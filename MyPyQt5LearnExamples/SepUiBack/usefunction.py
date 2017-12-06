# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'usefunction'
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
def show_string():
    str1 = ui.lineEdit.text()
    ui.textBrowser.setText(str1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = speUI.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 调用函数
    ui.pushButton.clicked.connect(show_string)

    MainWindow.show()
    sys.exit(app.exec_())
