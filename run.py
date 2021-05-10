import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QVBoxLayout, QStyledItemDelegate
from ui_main import Ui_MainWindow
from pycomm3 import LogixDriver
from PySide2.QtCore import QTimer, QThreadPool, QDateTime
from PySide2.QtCharts import QtCharts
from utils import resource_path
from datetime import datetime
import time
import csv
import json

from workers import Worker

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PySide2.QtWinExtras import QtWin
    myappid = 'wood.portapoll.1.0'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass
class DateTimeDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(DateTimeDelegate, self).initStyleOption(option, index)
        value = index.data()
        option.text = QDateTime.fromMSecsSinceEpoch(value).toString("dd.MM.yyyy")

class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PortaPoll")
        
        self.run_poll = True
        app.aboutToQuit.connect(self.thread_stop)

        self.ui.pushButton_poll.setStyleSheet("""
            QPushButton {
                background-color: red;
                color:white;    
            }   
            QPushButton:checked{
                background-color: rgb(35, 199, 35);
                border: none; 
            }
            QPushButton:hover{  
                background-color: grey; 
                border-style: outset;  
            }  
        """)

        with open(resource_path("config/settings.json")) as f:
            self.settings = json.load(f)

        self.ui.tableWidget.setColumnCount(len(self.settings["tags"]) + 1)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Date"))
        for i in range(0, len(self.settings["tags"])):
            self.ui.tableWidget.setHorizontalHeaderItem(i+1, QTableWidgetItem(self.settings["tags"][i]))
        
        self.ui.lineEdit_ip.setText(self.settings['default_ip'])
        self.ui.lineEdit_ip.editingFinished.connect(self.ip_change)
        self.ui.label_log_file.setText(self.settings["log_file"])
        self.ui.pushButton_log_file.clicked.connect(self.log_file)

        self.threadpool = QThreadPool().globalInstance()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.poller_thread()

        #self.chart_table()

    def chart_table(self):
        delegate = DateTimeDelegate(self.ui.tableWidget)
        self.ui.tableWidget.setItemDelegateForColumn(0, delegate)
        chart = QtCharts.QChart()
        self.chartView = QtCharts.QChartView(chart)
        self.chartView.setFixedSize(600, 430)

        layout = QVBoxLayout(self)
        layout.addWidget(self.chartView)
        self.ui.frame_chart.setLayout(layout)

        series = QtCharts.QLineSeries(name="Value")
        mapper = QtCharts.QVXYModelMapper(self, xColumn=0, yColumn=1)
        mapper.setModel(self.ui.tableWidget.model())
        mapper.setSeries(series)
        chart.addSeries(mapper.series())

        self.axis_X = QtCharts.QDateTimeAxis()
        self.axis_X.setFormat("MMM yyyy")
        self.axis_Y = QtCharts.QValueAxis()

        chart.setAxisX(self.axis_X, series)
        chart.setAxisY(self.axis_Y, series)
        self.axis_Y.setRange(0, 0)
        self.axis_Y.setLabelFormat("%.2f")
        chart.setTitle("Chart")
    
    def log_file(self):
        file_name = QFileDialog.getSaveFileName(self, "Save", "C:/Test Trailer Log.csv", "CSV (Comma delimited) (*.csv)")
        if file_name:
            self.ui.label_log_file.setText(file_name[0])
            self.settings["log_file"] = file_name[0]
            with open(resource_path("config/settings.json"), 'w') as f:
                json.dump(self.settings, f, indent=4)

    def ip_change(self):
        self.settings['default_ip'] = self.ui.lineEdit_ip.text()
        with open(resource_path("config/settings.json"), 'w') as f:
            json.dump(self.settings, f, indent=4)
    
    def thread_stop(self):
        self.run_poll = False

    def poller_thread(self):
        worker = Worker(self.poll_plc)
        self.threadpool.start(worker)

    def poll_plc(self):
        while self.run_poll:
            while self.ui.pushButton_poll.isChecked():
                if int(self.ui.label_countdown.text()) < 1:
                    self.ui.label_countdown.setText(str(self.ui.spinBox_poll.value()))
                    try:
                        
                        with LogixDriver(self.ui.lineEdit_ip.text()) as plc:
                            date_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            

                            row = self.ui.tableWidget.rowCount() - 1
                            if row >= 20:
                                self.ui.tableWidget.removeRow(row)
                            self.ui.tableWidget.insertRow(0)
                            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(date_stamp))

                            with open(self.ui.label_log_file.text(), "a", newline="") as outfile:
                                writer = csv.writer(outfile)
                                for i in self.settings["tags"]:
                                    fields = []
                                    fields.append(date_stamp)
                                    val = round(plc.read(i).value, 2)
                                    fields.append(i)
                                    fields.append(val)
                                    writer.writerow(fields)


                                    self.ui.tableWidget.setItem(0, self.settings["tags"].index(i)+1, QTableWidgetItem("%.2f" % val))
                    except Exception as error:
                        self.ui.label_error.setStyleSheet("background-color: rgba(255, 0, 0, 0.5);")
                        self.ui.label_error.setText(str(error))
                        time.sleep(10)
                    else:
                        self.ui.label_error.setStyleSheet("background-color: rgba(35, 199, 35, 1);")
                        self.ui.label_error.setText(" ")
                
                time.sleep(1)
                self.ui.label_countdown.setText(str(int(self.ui.label_countdown.text()) - 1))

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('images/sensor.ico'))
    window = MainWindow(app)
    window.show()
    sys.exit(app.exec_())