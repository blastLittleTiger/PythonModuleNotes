# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'useclass'
# __purpose__ =
# __author__ = 'prayjourney'
# __mtime__ = '2017/12/6'
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
import sys

from pyqt2nd import speUI
from PyQt5 import QtCore, QtWidgets, QtGui


#  使用函数的方式，来分离控制和UI


class mywindow(QtWidgets.QWidget, speUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = speUI.Ui_MainWindow()
        self.ui.setupUi(self)

    def show_string(self):
        str1 = self.lineEdit.text()
        self.textBrowser.setText(str1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    # ui = mywindow.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
    myshow = mywindow()
    myshow.show()
    sys.exit(app.exec_())
