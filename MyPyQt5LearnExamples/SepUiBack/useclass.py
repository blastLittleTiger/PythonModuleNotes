# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication

from pyqt2nd import speUI
from PyQt5 import QtCore, QtWidgets, QtGui


#  使用类继承的方式，来完成界面和逻辑的分离

class NewWindow(QtWidgets.QMainWindow, speUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_string)  # 信号

    def show_string(self):  # 槽函数
        str1 = self.lineEdit.text()
        self.textBrowser.setText(str1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = NewWindow()
    myshow.show()
    sys.exit(app.exec_())

    #  NoAttribuate问题的解决，主要是因为Qt Designer设计的APP,继承于QMainWindow而非QWidget
    #  https://stackoverflow.com/questions/43260595/attributeerror-ui-mainwindow-object-has-no-attribute-setcentralwidget-pyqt5
