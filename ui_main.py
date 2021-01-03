# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(816, 620)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 9, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 3, 1, 1)

        self.spinBox_poll = QSpinBox(self.centralwidget)
        self.spinBox_poll.setObjectName(u"spinBox_poll")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_poll.setFont(font)
        self.spinBox_poll.setMaximum(9999)
        self.spinBox_poll.setValue(60)

        self.gridLayout.addWidget(self.spinBox_poll, 2, 2, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 4)

        self.lineEdit_ip = QLineEdit(self.centralwidget)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setFont(font)

        self.gridLayout.addWidget(self.lineEdit_ip, 1, 1, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 2)

        self.pushButton_poll = QPushButton(self.centralwidget)
        self.pushButton_poll.setObjectName(u"pushButton_poll")
        self.pushButton_poll.setFont(font)
        self.pushButton_poll.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_poll, 3, 1, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_2.addWidget(self.tableWidget, 6, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setFont(font)

        self.gridLayout_2.addWidget(self.label_error, 7, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 816, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PortaPoll", None))
        self.lineEdit_ip.setText(QCoreApplication.translate("MainWindow", u"192.168.1.103", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Poll Frequency (Seconds)", None))
        self.pushButton_poll.setText(QCoreApplication.translate("MainWindow", u"Poll", None))
        self.label_error.setText("")
    # retranslateUi

