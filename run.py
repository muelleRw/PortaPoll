# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_main import Ui_MainWindow
from pycomm3 import LogixDriver
from PySide2.QtCore import QTimer, QThreadPool
from datetime import datetime
import time
import csv

from workers import Worker

try:
    # Include in try/except block if you're also targeting Mac/Linux
    from PySide2.QtWinExtras import QtWin
    myappid = 'mycompany.myproduct.subproduct.version'
    QtWin.setCurrentProcessExplicitAppUserModelID(myappid)    
except ImportError:
    pass


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PortaPoll")
        self.ui.pushButton_poll.setStyleSheet("""
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

        with open("C:/Users/Dell/Documents/test trailer log.csv", "r") as f:
            reader = csv.reader(f)
            self.columns = list(next(reader))

        self.ui.tableWidget.setColumnCount(len(self.columns))
        for i in range(0, len(self.columns)):
            self.ui.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(self.columns[i]))

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.poller_thread()
    
    def poller_thread(self):
        worker = Worker(self.poll_plc)

        #worker.signals.result.connect(self.print_output)
        #worker.signals.finished.connect(self.thread_complete)
        #worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def poll_plc(self):
        while True:
            while self.ui.pushButton_poll.isChecked():
                try:
                    fields = []
                    with LogixDriver(self.ui.lineEdit_ip.text()) as plc:
                        date_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        fields.append(date_stamp)
                        for i in range(1, len(self.columns)):
                            fields.append(round(plc.read(self.columns[i]).value, 2))

                        self.ui.label_error.setStyleSheet("background-color: rgba(35, 199, 35, 1);")
                        self.ui.label_error.setText(" ")

                        with open("C:/Users/Dell/Documents/test trailer log.csv", "a", newline="") as outfile:
                            writer = csv.writer(outfile)
                            writer.writerow(fields)
                    row = self.ui.tableWidget.rowCount() - 1
                    
                    if row >= 20:
                        self.ui.tableWidget.removeRow(row - 1)
                    self.ui.tableWidget.insertRow(0)
                    self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(date_stamp))
                    for i in range(1, len(fields)):
                        self.ui.tableWidget.setItem(0, i, QTableWidgetItem("%.2f" % fields[i]))

                except Exception as error:
                    self.ui.label_error.setStyleSheet("background-color: rgba(255, 0, 0, 0.5);")
                    self.ui.label_error.setText(str(error))
                    time.sleep(10)
                else:
                    pass
                
                time.sleep(self.ui.spinBox_poll.value())

        

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('fire.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
