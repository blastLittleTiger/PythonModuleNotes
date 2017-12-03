# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstPyQtui.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(284, 233)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 130, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 90, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 284, 23))
        self.menubar.setObjectName("menubar")
        self.menu_123 = QtWidgets.QMenu(self.menubar)
        self.menu_123.setObjectName("menu_123")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionHello = QtWidgets.QAction(mainWindow)
        self.actionHello.setObjectName("actionHello")
        self.actiontuichu = QtWidgets.QAction(mainWindow)
        self.actiontuichu.setObjectName("actiontuichu")
        self.menu_123.addAction(self.actionHello)
        self.menu.addAction(self.actiontuichu)
        self.menubar.addAction(self.menu_123.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.pushButton.setText(_translate("mainWindow", "确定"))
        self.label.setText(_translate("mainWindow", "姓名："))
        self.label_2.setText(_translate("mainWindow", "年龄："))
        self.menu_123.setTitle(_translate("mainWindow", "菜单"))
        self.menu.setTitle(_translate("mainWindow", "退出"))
        self.actionHello.setText(_translate("mainWindow", "Hello"))
        self.actiontuichu.setText(_translate("mainWindow", "退出"))

