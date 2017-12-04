# coding:utf-8

import sys
from PyQt5 import QtCore,QtWidgets,QtGui
from mypyqt5 import ComplexUI

class MainWindow(object):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ComplexUI.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.update_date()
        self.update_calendar()
        self.set_dial()
        self.click_radio1()
        self.click_radio2()
        self.click_radio3()
        self.set_dial2()
        self.set_font()
        MainWindow.show()
        sys.exit(app.exec_())

    # 修改日期修改器数值
    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())

    # 日历信号槽
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    # 设置LCD数字
    def set_lcd(self):
        self.ui.lcdNumber.display(self.ui.dial.value())

    # 刻度盘信号槽
    def set_dial(self):
        self.ui.dial.valueChanged['int'].connect(self.set_lcd)

    # 设置默认
    def click_radio1(self):
        self.ui.radioButton.clicked.connect(self.click_radio1_default)

    def click_radio1_default(self):
        self.ui.progressBar.setValue(60)

    # 设置清零
    def click_radio2(self):
        self.ui.radioButton_2.clicked.connect(self.ui.progressBar.reset)

    # 关联lcd number
    def click_radio3(self):
        self.ui.radioButton_3.clicked.connect(self.update_process_radio3)

    # 更新进度栏使用radio3
    def update_process_radio3(self):
        value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(value)

    # 更新进度栏使用dial
    def set_dial2(self):
        self.ui.dial.valueChanged['int'].connect(self.update_process_dial)

    def update_process_dial(self):
        value = self.ui.dial.value()
        self.ui.progressBar.setValue(value)

    # 更新字体
    def set_font(self):
        self.ui.fontComboBox.activated['QString'].connect(self.ui.label.setText)



if __name__ == "__main__":
    MainWindow() # 新建的对象，创建好了之后执行__init__()
