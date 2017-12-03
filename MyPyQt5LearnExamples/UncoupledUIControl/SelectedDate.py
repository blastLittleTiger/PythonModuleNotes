# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectedDate.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 285)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/图片/图标/calendar1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.cal_widget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.cal_widget.setGeometry(QtCore.QRect(60, 10, 248, 197))
        self.cal_widget.setObjectName("cal_widget")
        self.lb_selected = QtWidgets.QLabel(self.centralwidget)
        self.lb_selected.setGeometry(QtCore.QRect(60, 220, 71, 16))
        self.lb_selected.setObjectName("lb_selected")
        self.le_date = QtWidgets.QLineEdit(self.centralwidget)
        self.le_date.setGeometry(QtCore.QRect(150, 220, 161, 20))
        self.le_date.setObjectName("le_date")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "选中的日期"))
        self.lb_selected.setText(_translate("MainWindow", "选中的日期："))

