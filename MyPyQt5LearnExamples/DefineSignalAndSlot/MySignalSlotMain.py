# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'MySignalSlotMain'
# __purpose__ =
# __author__ = 'prayjourney'
# __mtime__ = '2017/12/7'
# __copyright__='(c) renjiaxin.jesse 2017'
# __licence__ = 'prayjourney 2017'
# 
#                 ┏ ┓   ┏ ┓
#              ┏━━┛ ┻━━━┛ ┻━━┓
#              ┃    #
#              ┃   ┳┛  ┗*━   ┃    蹉跎错，消磨过，最是光阴化浮沫。
#              ┃      ┻      ┃
#              ┗━━┓       ┏━━┛
#                 ┃         ┗━━━━━━━━━━┓
#                 ┃  神兽保佑           ┣━┓
#                 ┃  永无BUG！         ┏┛
#                 ┗┓━┓ ┏━━━━━━━━━┳━┓━┓┛
#                  ┃━┫━┫         ┃━┫━┫
#                  ┗━┻━┛         ┗━┻━┛
#
# ---------------------------------------------------------------

'''
1.创建信号--->2.关联槽函数--->3.等待时机发射信号
'''
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication

from pyqt2nd import MySignalSlot


class MyWindow(QtWidgets.QMainWindow, MySignalSlot.Ui_mainWindow):
    # 自定义的signal，带有参数，Python基本类型的数据均可
    addSignal = pyqtSignal(list, str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # 这个不能放在connect下面语句之后，不然没有初始化成功
        self.addSignal[list, str].connect(self.addParameter)  # 关联槽函数
        self.pushButton.clicked.connect(self.emitAddSignal)  # 等待时机发射信号，创造发射机会

    # 槽函数
    def addParameter(self, ls, st):
        value = str(ls[0]) + str(ls[1])
        self.textEdit.setText(value + st)

    # 此处发射信号，使用该信号，发射的时候，携带上参数
    def emitAddSignal(self):
        if self.lineEdit_1.text() != "" and self.lineEdit_2.text() != "":
            plist = []
            plist.append(self.lineEdit_1.text())
            plist.append(self.lineEdit_2.text())
            self.addSignal.emit(plist, ",是相加的结果.")  # 使用该信号，发射的时候，携带参数


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    sys.exit(app.exec_())
