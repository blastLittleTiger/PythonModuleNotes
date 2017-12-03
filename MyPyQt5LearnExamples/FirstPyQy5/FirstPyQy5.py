# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mypyqt5'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!
import sys
import mypyqt5.FirstPyQtui as FirstPyQtui
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = FirstPyQtui.Ui_mainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
