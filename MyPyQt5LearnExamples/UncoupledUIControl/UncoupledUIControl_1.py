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
from mypyqt5 import SelectedDate
from PyQt5 import QtCore, QtWidgets, QtGui


#  使用函数的方式，来分离控制和UI

def show_date(date):
    ui.le_date.setText(date.toString())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SelectedDate.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 调用函数
    ui.cal_widget.clicked[QDate].connect(show_date)

    MainWindow.show()
    sys.exit(app.exec_())
