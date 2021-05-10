import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QVBoxLayout, QStyledItemDelegate
from ui_main import Ui_MainWindow
from pycomm3 import LogixDriver
from PySide2.QtCore import QTimer, QThreadPool, QDateTime
from PySide2.QtCharts import QtCharts
from utils import resource_path
from datetime import datetime, timedelta
import time
import csv
import json

from workers import Worker

from pyqtgraph import PlotWidget, plot, DateAxisItem
import pyqtgraph as pg
from random import randint

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PySide2.QtWinExtras import QtWin
    myappid = 'wood.portapoll.1.0'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass
class TimeAxisItem(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        return [datetime.fromtimestamp(value) for value in values]

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
            self.ui.comboBox_chart_tag.addItem(self.settings["tags"][i])
        
        self.ui.lineEdit_ip.setText(self.settings['default_ip'])
        self.ui.lineEdit_ip.editingFinished.connect(self.ip_change)
        self.ui.label_log_file.setText(self.settings["log_file"])
        self.ui.pushButton_log_file.clicked.connect(self.log_file)

        self.threadpool = QThreadPool().globalInstance()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.poller_thread()

        self.chart_table()

    def chart_table(self):
        #base = datetime.today()
        #self.x = [base - timedelta(seconds=x) for x in range(20)]  # 100 time points
        self.x=[]
        self.y=[]
        #self.y = [0 for _ in range(20)]  # 100 data points

        date_axis = TimeAxisItem(orientation='bottom')
        self.graph = pg.PlotWidget(axisItems = {'bottom': date_axis})
        #self.graph.plot(x=[x.timestamp() for x in self.x], y=self.y, clear=True)

        layout = QVBoxLayout(self)
        layout.addWidget(self.graph)
        self.ui.frame_chart.setLayout(layout)
        
    def refresh_chart(self):
        pen = pg.mkPen(color=(255, 0, 0))
        self.graph.plot(x=[x.timestamp() for x in self.x], y=self.y, pen=pen, clear=True)

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
                            curr_datetime = datetime.now()
                            date_stamp = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
                            
                            
                            row = self.ui.tableWidget.rowCount()
                            if row >= self.ui.spinBox_chart_points.value():
                                self.ui.tableWidget.removeRow(row-1)
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

                                    if i == self.ui.comboBox_chart_tag.currentText():
                                        self.x.append(curr_datetime)
                                        self.y.append(val)
                                        if len(self.x) > self.ui.spinBox_chart_points.value():
                                            self.x.pop(0)
                                        if len(self.y) > self.ui.spinBox_chart_points.value():
                                            self.y.pop(0)
                                        self.refresh_chart()

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