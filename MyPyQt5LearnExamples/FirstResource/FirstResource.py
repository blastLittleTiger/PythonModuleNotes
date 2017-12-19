# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QWindow, QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication
from pyqt2nd import ResourceUse
from pyqt2nd import res2_rc  # 需要导入，不然显示有问题
"""
使用Resource的一个好处就是，我们可以将资源如图片，编译成16进制的文件
这样，在文件丢失或者我们运行的环境转移的情况之下，使用Resource仍然可以
获取到我们所需要的资源，而不必太过于担忧资源丢失的风险
"""

class FirstResource(QtWidgets.QMainWindow, ResourceUse.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.secondinit()

    # 通过资源文件自定义的设置图标
    def secondinit(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/image/snow.ico"))
        self.setWindowIcon(icon)
        # 设置窗口背景
        pixmap = QPixmap(":/newPrefix/image/mnv.jpg").scaled(self.size())  # 适应窗口大小
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    useresource = FirstResource()
    useresource.show()
    sys.exit(app.exec_())
