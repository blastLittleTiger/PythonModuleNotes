# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 
# __title__ = 'DefineSignalSlot'
# __purpose__ =
# __author__ = 'prayjourney'
# __mtime__ = '2017/12/5'
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
from PyQt5.QtCore import QObject, pyqtSignal


class NewSignal(QObject):
    # 一个valueChanged的信号，该信号没有参数.
    valueChanged = pyqtSignal()

    def connect_and_emit_valueChanged(self):
        # 绑定信号和槽函数
        self.valueChanged.connect(self.handle_valueChanged)

        # 发射信号.
        self.trigger.emit()

    def handle_valueChanged(self):
        print("trigger signal received")
