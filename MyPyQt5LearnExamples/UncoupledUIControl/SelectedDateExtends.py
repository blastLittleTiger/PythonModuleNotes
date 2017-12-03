# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'SelectedDateExtends'
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
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow

from mypyqt5.SelectedDate import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        # 为啥这样不行呢？
        self.cal_widget.clicked[QDate].connect(self.show_date)

    def show_date(self, date):
        self.le_date.setText(date.toString())
