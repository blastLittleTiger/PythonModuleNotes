# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LookInfoDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 140)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 80, 301, 32))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lb_info = QtWidgets.QLabel(Dialog)
        self.lb_info.setGeometry(QtCore.QRect(40, 40, 55, 20))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.lb_info.setFont(font)
        self.lb_info.setObjectName("lb_info")
        self.lb_text = QtWidgets.QLabel(Dialog)
        self.lb_text.setGeometry(QtCore.QRect(110, 40, 240, 20))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.lb_text.setFont(font)
        self.lb_text.setText("")
        self.lb_text.setObjectName("lb_text")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_info.setText(_translate("Dialog", "信息："))

