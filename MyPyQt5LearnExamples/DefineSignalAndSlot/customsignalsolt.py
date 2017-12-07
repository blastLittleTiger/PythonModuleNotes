# -*- coding:utf-8 -*-


'''
自定义信号和槽函数
'''

'''
# 创建自定义的槽和信号
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import *
import sys

class Test(QDialog):
    button_clicked_signal = pyqtSignal()  # 自定义信号，不带参

    def __init__(self, parent=None):
        super().__init__(parent)

        btn = QPushButton('关闭', self)
        btn.clicked.connect(self.btn_clicked)  # 信号/槽

        self.button_clicked_signal.connect(self.my_close)  # 接收信号，连接到槽

    def btn_clicked(self):
        self.button_clicked_signal.emit()  # 发送自定义信号，无参

    def my_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Test()
    dlg.show()
    sys.exit(app.exec_())

'''

# from PyQt5.QtCore import QObject, pyqtSignal
#
# class NewSignal(QObject):
#
#     # 一个valueChanged的信号，该信号没有参数.
#     valueChanged = pyqtSignal()
#
#     def connect_and_emit_valueChanged(self):
#         # 绑定信号和槽函数
#         self.valueChanged.connect(self.handle_valueChanged)
#
#         # 发射信号.
#         self.trigger.emit()
#
#     def handle_valueChanged(self):
#         print("trigger signal received")

# 核心在于，创建一个信号，然后将信号和一个处理的槽函数绑定，符合一定的条件的时候，就将信号发射
# 比如下面的printSignal = pyqtSignal(list)，此处定义了信号，self.printSignal.connect(self.printPaper)
# 在此处将信号和槽函数连接起来，然后最后所需要的就是等待时机，将信号发射
# self.printButton.clicked.connect(self.emitPrintSignal)这个就是信号发射的函数，其实现如下：
#     def emitPrintSignal(self):
#         pList = []
#         pList.append(self.numberSpinBox.value())
#         pList.append(self.styleCombo.currentText())
#         self.printSignal.emit(pList)
# 整个流程如下：
# 1.创建信号--->2.关联槽函数--->等待时机发射信号



import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, \
    QComboBox, QGridLayout


class SignalEmit(QWidget):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    # 声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.creatContorls("打印控制：")
        self.creatResult("操作结果：")

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)

        self.helpSignal.connect(self.showHelpMessage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('defined signal')
        self.show()

    def creatContorls(self, title):
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("打印")
        self.previewButton = QPushButton("预览")
        numberLabel = QLabel("打印份数：")
        pageLabel = QLabel("纸张类型：")
        self.previewStatus = QCheckBox("全屏预览")
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(1, 100)
        self.styleCombo = QComboBox(self)
        self.styleCombo.addItem("A4")
        self.styleCombo.addItem("A5")

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        controlsLayout.addWidget(pageLabel, 0, 2)
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        controlsLayout.addWidget(self.printButton, 0, 4)
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        controlsLayout.addWidget(self.previewButton, 3, 1)
        self.controlsGroup.setLayout(controlsLayout)

    def creatResult(self, title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)

    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int, str].emit(1080, " Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")

    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self, list):
        self.resultLabel.setText("Print: " + "份数：" + str(list[0]) + "  纸张：" + str(list[1]))

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    def previewPaper(self, text):
        self.resultLabel.setText(text)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    def showHelpMessage(self, message):
        self.resultLabel.setText(message)
        # self.statusBar().showMessage(message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())
