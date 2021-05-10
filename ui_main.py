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
        MainWindow.resize(931, 795)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.tableWidget = QTableWidget(self.centralwidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(0, 250))

        self.gridLayout_2.addWidget(self.tableWidget, 8, 0, 1, 2)

        self.frame_chart = QFrame(self.centralwidget)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setMinimumSize(QSize(0, 250))
        self.frame_chart.setFrameShape(QFrame.Box)
        self.frame_chart.setFrameShadow(QFrame.Plain)
        self.frame_chart.setLineWidth(2)

        self.gridLayout_2.addWidget(self.frame_chart, 5, 0, 1, 2)

        self.label_error = QLabel(self.centralwidget)
        self.label_error.setObjectName(u"label_error")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_error.setFont(font)

        self.gridLayout_2.addWidget(self.label_error, 9, 0, 1, 2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.label_log_file = QLabel(self.centralwidget)
        self.label_log_file.setObjectName(u"label_log_file")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_log_file.setFont(font2)

        self.gridLayout.addWidget(self.label_log_file, 2, 1, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 4, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.pushButton_log_file = QPushButton(self.centralwidget)
        self.pushButton_log_file.setObjectName(u"pushButton_log_file")
        self.pushButton_log_file.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_log_file)


        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_ip = QLineEdit(self.centralwidget)
        self.lineEdit_ip.setObjectName(u"lineEdit_ip")
        self.lineEdit_ip.setFont(font)

        self.horizontalLayout_3.addWidget(self.lineEdit_ip)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 5)

        self.pushButton_poll = QPushButton(self.centralwidget)
        self.pushButton_poll.setObjectName(u"pushButton_poll")
        self.pushButton_poll.setFont(font)
        self.pushButton_poll.setCheckable(True)

        self.gridLayout.addWidget(self.pushButton_poll, 4, 1, 1, 3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.spinBox_poll = QSpinBox(self.centralwidget)
        self.spinBox_poll.setObjectName(u"spinBox_poll")
        self.spinBox_poll.setFont(font)
        self.spinBox_poll.setMaximum(9999)
        self.spinBox_poll.setValue(60)

        self.horizontalLayout_4.addWidget(self.spinBox_poll)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.horizontalLayout.addWidget(self.label_4)

        self.label_countdown = QLabel(self.centralwidget)
        self.label_countdown.setObjectName(u"label_countdown")
        self.label_countdown.setFont(font)

        self.horizontalLayout.addWidget(self.label_countdown)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.comboBox_chart_tag = QComboBox(self.centralwidget)
        self.comboBox_chart_tag.setObjectName(u"comboBox_chart_tag")
        self.comboBox_chart_tag.setFont(font)

        self.horizontalLayout_7.addWidget(self.comboBox_chart_tag)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.spinBox_chart_points = QSpinBox(self.centralwidget)
        self.spinBox_chart_points.setObjectName(u"spinBox_chart_points")
        self.spinBox_chart_points.setFont(font)
        self.spinBox_chart_points.setMaximum(99999)
        self.spinBox_chart_points.setValue(1440)

        self.horizontalLayout_6.addWidget(self.spinBox_chart_points)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)


        self.gridLayout.addLayout(self.horizontalLayout_9, 3, 0, 1, 5)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 931, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_ip, self.pushButton_log_file)
        QWidget.setTabOrder(self.pushButton_log_file, self.spinBox_poll)
        QWidget.setTabOrder(self.spinBox_poll, self.comboBox_chart_tag)
        QWidget.setTabOrder(self.comboBox_chart_tag, self.spinBox_chart_points)
        QWidget.setTabOrder(self.spinBox_chart_points, self.pushButton_poll)
        QWidget.setTabOrder(self.pushButton_poll, self.tableWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_error.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"PortaPoll", None))
        self.label_log_file.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.pushButton_log_file.setText(QCoreApplication.translate("MainWindow", u"Log File", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"IP Address", None))
        self.pushButton_poll.setText(QCoreApplication.translate("MainWindow", u"Poll", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Poll Seconds", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Poll Countdown:", None))
        self.label_countdown.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Chart Tag", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Chart Points", None))
    # retranslateUi

