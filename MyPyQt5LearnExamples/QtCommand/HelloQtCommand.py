# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloQtCommand.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mypyqt5 import LookInfoDlg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/图片/图标/rainbow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_username = QtWidgets.QLabel(self.centralwidget)
        self.lb_username.setGeometry(QtCore.QRect(30, 40, 54, 20))
        self.lb_username.setObjectName("lb_username")
        self.le_username = QtWidgets.QLineEdit(self.centralwidget)
        self.le_username.setGeometry(QtCore.QRect(80, 40, 191, 20))
        self.le_username.setObjectName("le_username")
        self.lb_password = QtWidgets.QLabel(self.centralwidget)
        self.lb_password.setGeometry(QtCore.QRect(30, 90, 54, 20))
        self.lb_password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_password.setObjectName("lb_password")
        self.le_password = QtWidgets.QLineEdit(self.centralwidget)
        self.le_password.setGeometry(QtCore.QRect(80, 90, 191, 20))
        self.le_password.setObjectName("le_password")
        self.pbt_cancle = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_cancle.setGeometry(QtCore.QRect(120, 140, 60, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/图片/图标/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_cancle.setIcon(icon1)
        self.pbt_cancle.setObjectName("pbt_cancle")
        self.pbt_okay = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_okay.setGeometry(QtCore.QRect(210, 140, 60, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/图片/图标/okay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_okay.setIcon(icon2)
        self.pbt_okay.setObjectName("pbt_okay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_create = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/图片/图标/create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_create.setIcon(icon3)
        self.act_create.setObjectName("act_create")
        self.act_exit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:/图片/图标/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon4)
        self.act_exit.setObjectName("act_exit")
        self.act_exit2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:/图片/图标/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit2.setIcon(icon5)
        self.act_exit2.setObjectName("act_exit2")
        self.menu.addAction(self.act_create)
        self.menu.addAction(self.act_exit)
        self.menu_2.addAction(self.act_exit2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        # 修改方法，并连接到号槽上面
        # 原始的方法
        # http://zmister.com/archives/162.html
        # self.pbt_cancle.clicked.connect(self.le_password.clear())
        self.pbt_cancle.clicked.connect(self.setwords)
        self.act_exit.triggered.connect(MainWindow.close)
        self.act_exit2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定一个弹出对话框
        self.pbt_okay.clicked.connect(self.btnokay)

    # 我们设置的方法
    def setwords(self):
        self.le_password.setText("请输入密码！")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "带图标的UI"))
        self.lb_username.setText(_translate("MainWindow", "用户名："))
        self.lb_password.setText(_translate("MainWindow", "密  码："))
        self.pbt_cancle.setText(_translate("MainWindow", "取消"))
        self.pbt_okay.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "退出"))
        self.act_create.setText(_translate("MainWindow", "新文件"))
        self.act_exit.setText(_translate("MainWindow", "退出"))
        self.act_exit.setStatusTip(_translate("MainWindow", "点击退出应用程序"))
        self.act_exit2.setText(_translate("MainWindow", "退出"))

    # 这是为弹出对话框而准备的方法
    def btnokay(self):
        Dialog = QtWidgets.QDialog()
        ui1 = LookInfoDlg.Ui_Dialog()
        ui1.setupUi(Dialog)
        str1 = self.le_username.text()
        str2 = self.le_password.text()
        # 此处不能是self，因为self表示的是mainwindow上面的控件
        # 这是将一个数据从一个控件，传送到另一个控件上面显示
        ui1.lb_text.setText("用户名：" + str1 + "，密码：" + str2)
        Dialog.show()
        Dialog.exec_()
