from PyQt5 import QtWidgets, QtGui
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QWindow, QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication
from pyqt2nd import ResourceUse
from pyqt2nd import res2_rc  # 需要导入，不然显示有问题


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
