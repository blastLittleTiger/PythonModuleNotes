# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow

from mypyqt5.SelectedDate import Ui_MainWindow


# 继承的类

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # super().__init__(parent)
        self.setupUi(self)

        self.cal_widget.clicked[QDate].connect(self.show_date)

    def show_date(self, date):
        self.le_date.setText(date.toString())
