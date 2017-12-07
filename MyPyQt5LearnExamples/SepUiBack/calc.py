# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-


from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget

from pyqt2nd.calc_ui import Ui_Calc


# 方式一
# class MyCalc(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.ui = Ui_Calc()
#         self.ui.setupUi(self)
#
#     @pyqtSlot(int)
#     def on_inputSpinBox1_valueChanged(self, value):
#         self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox2.value()))
#
#     @pyqtSlot(int)
#     def on_inputSpinBox2_valueChanged(self, value):
#         self.ui.outputWidget.setText(str(value + self.ui.inputSpinBox1.value()))


# 方式二
# class MyCalc2(QWidget, Ui_Calc):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)
#
#     @pyqtSlot(int)
#     def on_inputSpinBox1_valueChanged(self, value):
#         self.outputWidget.setText(str(value + self.inputSpinBox2.value()))
#
#     @pyqtSlot(int)
#     def on_inputSpinBox2_valueChanged(self, value):
#         self.outputWidget.setText(str(value + self.inputSpinBox1.value()))


# 方式三
class MyCalc3(QWidget, Ui_Calc):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.inputSpinBox1.valueChanged.connect(self.setText1)  # 这样也是可以的，但是明显使用上面的方法更加方便
        self.inputSpinBox2.valueChanged.connect(self.setText2)

    def setText1(self):
        value = self.inputSpinBox1.value()
        self.outputWidget.setText(str(value + self.inputSpinBox2.value()))

    def setText2(self):
        value = self.inputSpinBox2.value()
        self.outputWidget.setText(str(value + self.inputSpinBox1.value()))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # win = MyCalc()
    # win = MyCalc2()
    win = MyCalc3()
    win.show()
    sys.exit(app.exec_())

    # https://www.cnblogs.com/hhh5460/p/5390999.html
    # http://blog.csdn.net/mr_zing/article/details/46945011
