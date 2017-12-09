# -*- coding: utf-8 -*-

import sys
from mypyqt5 import SelectedDateExtends
from PyQt5 import QtCore, QtWidgets, QtGui

#  使用类继承的方式，来分离控制和UI
#  此处用来控制，完全将控制和UI分离了，原始的UI:SelectedDate,继承的UI:SelectedDateExtends,本文件为控制文件

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    newwindow = SelectedDateExtends.MainWindow()  # 此处只需要新的类来完成出创建和显示即可
    newwindow.show()
    sys.exit(app.exec_())
