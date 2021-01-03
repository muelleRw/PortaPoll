# This Python file uses the following encoding: utf-8
import sys
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTreeWidgetItem
from PySide2.QtCore import Qt
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

        self.ui.treeWidget.setColumnCount(2)
        self.ui.treeWidget.setHeaderLabels(["Tag", "Type"])
        self.ui.treeWidget.setSortingEnabled(True)
        self.tags = []
        self.poll_tags = []
        self.ui.lineEdit_ip.editingFinished.connect(self.get_plc_tags)

        #self.ui.tableWidget.setColumnCount(len(self.columns))
        #for i in range(0, len(self.columns)):
        #    self.ui.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(self.columns[i]))

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.poller_thread()

    def find_checked(self):
        for i in range(0, self.ui.treeWidget.topLevelItemCount()):
            if self.ui.treeWidget.topLevelItem(i).checkState(0) == Qt.CheckState.Checked:
                #print(self.ui.treeWidget.topLevelItem(i).text(0))
                self.poll_tags.append(self.ui.treeWidget.topLevelItem(i).text(0))
        self.ui.tableWidget.setColumnCount(len(self.poll_tags) + 1)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Date"))
        for i in range(0, len(self.poll_tags)):
            self.ui.tableWidget.setHorizontalHeaderItem(i + 1, QTableWidgetItem(self.poll_tags[i]))
                #print(self.ui.treeWidget.topLevelItem(i).columnCount())
       

    def get_plc_tags(self):
        self.tags.clear()
        self.ui.treeWidget
        with LogixDriver(self.ui.lineEdit_ip.text()) as plc:
            self.tags = plc.get_tag_list()
        for i in self.tags:
            parent = QTreeWidgetItem(self.ui.treeWidget)
            parent.setText(0, "{}".format(i['tag_name']))
            if type(i['data_type']) == str:
                parent.setText(1, i['data_type'])
            parent.setFlags(parent.flags() | Qt.ItemIsUserCheckable)
            parent.setCheckState(0, Qt.Unchecked)
                #for x in range(5):
                #    child = QTreeWidgetItem(parent)
                #    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                #    child.setText(0, "Child {}".format(x))
                #    child.setCheckState(0, Qt.Unchecked)
        
        self.ui.treeWidget.sortByColumn(0)
        self.ui.treeWidget.resizeColumnToContents(0)
    
    def poller_thread(self):
        worker = Worker(self.poll_plc)
        #worker.signals.result.connect(self.print_output)
        #worker.signals.finished.connect(self.thread_complete)
        #worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(worker)

    def poll_plc(self):
        while True:
            while self.ui.pushButton_poll.isChecked():
                self.find_checked()
                
                try:
                    fields = []
                    with LogixDriver(self.ui.lineEdit_ip.text()) as plc:
                        date_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        fields.append(date_stamp)

                        row = self.ui.tableWidget.rowCount() - 1
                        if row >= 20:
                            self.ui.tableWidget.removeRow(row - 1)
                        self.ui.tableWidget.insertRow(0)
                        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(date_stamp))

                        with open("test.csv", "a", newline="") as outfile:
                            writer = csv.writer(outfile)
                            for i in self.poll_tags:
                                val = round(plc.read(self.poll_tags[i] + ".EuOut").value, 2)
                                fields.append(self.poll_tags[i])
                                fields.append(val)
                                writer.writerow(fields)

                                self.ui.tableWidget.setItem(0, i, QTableWidgetItem("%.2f" % val))
                        #for i in self.poll_tags:
                        #    fields.append(plc.read(self.poll_tags[i] + ".EuOut").value)

                except Exception as error:
                    self.ui.label_error.setStyleSheet("background-color: rgba(255, 0, 0, 0.5);")
                    self.ui.label_error.setText(str(error))
                    time.sleep(10)
                else:
                    self.ui.label_error.setStyleSheet("background-color: rgba(35, 199, 35, 1);")
                    self.ui.label_error.setText(" ")
                    
                time.sleep(self.ui.spinBox_poll.value())

        

if __name__ == "__main__":
    app = QApplication([])
    app.setWindowIcon(QIcon('fire.ico'))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
