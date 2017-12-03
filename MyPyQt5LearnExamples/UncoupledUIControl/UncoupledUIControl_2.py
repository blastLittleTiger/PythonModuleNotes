# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'UncoupledUIControl'
# __purpose__ =
# __author__ = 'prayjourney'
# __mtime__ = '2017/12/3'
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
from PyQt5.QtCore import QDate
from mypyqt5 import SelectedDateExtends
from PyQt5 import QtCore, QtWidgets, QtGui

#  使用类继承的方式，来分离控制和UI

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SelectedDateExtends.MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
