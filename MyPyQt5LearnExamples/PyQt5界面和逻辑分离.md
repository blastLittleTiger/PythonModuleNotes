###PyQt5界面和逻辑分离

***

#####初步的方式
我们使用Qt Desginer创建好了UI文件之后，通过PyUIC将UI文件转换成py文件之后，可以在此界面文件之中进行按钮响应，文字更改，进度更改等操作，如，我们在一个界面输入信息，点击确定之后，将信息显示到对话框之中，如下显示的是主界面，文件名为*HelloQtCommand.py*，代码之中包含了对于按钮事件的响应

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HelloQtCommand.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from mypyqt5 import LookInfoDlg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 240)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("F:/图片/图标/rainbow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_username = QtWidgets.QLabel(self.centralwidget)
        self.lb_username.setGeometry(QtCore.QRect(30, 40, 54, 20))
        self.lb_username.setObjectName("lb_username")
        self.le_username = QtWidgets.QLineEdit(self.centralwidget)
        self.le_username.setGeometry(QtCore.QRect(80, 40, 191, 20))
        self.le_username.setObjectName("le_username")
        self.lb_password = QtWidgets.QLabel(self.centralwidget)
        self.lb_password.setGeometry(QtCore.QRect(30, 90, 54, 20))
        self.lb_password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lb_password.setObjectName("lb_password")
        self.le_password = QtWidgets.QLineEdit(self.centralwidget)
        self.le_password.setGeometry(QtCore.QRect(80, 90, 191, 20))
        self.le_password.setObjectName("le_password")
        self.pbt_cancle = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_cancle.setGeometry(QtCore.QRect(120, 140, 60, 20))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("F:/图片/图标/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_cancle.setIcon(icon1)
        self.pbt_cancle.setObjectName("pbt_cancle")
        self.pbt_okay = QtWidgets.QPushButton(self.centralwidget)
        self.pbt_okay.setGeometry(QtCore.QRect(210, 140, 60, 20))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("F:/图片/图标/okay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbt_okay.setIcon(icon2)
        self.pbt_okay.setObjectName("pbt_okay")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.act_create = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("F:/图片/图标/create.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_create.setIcon(icon3)
        self.act_create.setObjectName("act_create")
        self.act_exit = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("F:/图片/图标/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit.setIcon(icon4)
        self.act_exit.setObjectName("act_exit")
        self.act_exit2 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("F:/图片/图标/exit2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_exit2.setIcon(icon5)
        self.act_exit2.setObjectName("act_exit2")
        self.menu.addAction(self.act_create)
        self.menu.addAction(self.act_exit)
        self.menu_2.addAction(self.act_exit2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        # 修改方法，并连接到号槽上面
        # 原始的方法
        # http://zmister.com/archives/162.html
        # self.pbt_cancle.clicked.connect(self.le_password.clear())
        self.pbt_cancle.clicked.connect(self.setwords)
        self.act_exit.triggered.connect(MainWindow.close)
        self.act_exit2.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 绑定一个弹出对话框
        self.pbt_okay.clicked.connect(self.btnokay)

    # 我们设置的方法
    def setwords(self):
        self.le_password.setText("请输入密码！")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "带图标的UI"))
        self.lb_username.setText(_translate("MainWindow", "用户名："))
        self.lb_password.setText(_translate("MainWindow", "密  码："))
        self.pbt_cancle.setText(_translate("MainWindow", "取消"))
        self.pbt_okay.setText(_translate("MainWindow", "确定"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.menu_2.setTitle(_translate("MainWindow", "退出"))
        self.act_create.setText(_translate("MainWindow", "新文件"))
        self.act_exit.setText(_translate("MainWindow", "退出"))
        self.act_exit.setStatusTip(_translate("MainWindow", "点击退出应用程序"))
        self.act_exit2.setText(_translate("MainWindow", "退出"))

    # 这是为弹出对话框而准备的方法
    def btnokay(self):
        Dialog = QtWidgets.QDialog()
        ui1 = LookInfoDlg.Ui_Dialog()
        ui1.setupUi(Dialog)
        str1 = self.le_username.text()
        str2 = self.le_password.text()
        # 此处不能是self，因为self表示的是mainwindow上面的控件
        # 这是将一个数据从一个控件，传送到另一个控件上面显示
        ui1.lb_text.setText("用户名：" + str1 + "，密码：" + str2)
        Dialog.show()
        Dialog.exec_()

```

显示效果如图
![inputinfo](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_inputinfo.jpg)

此处是显示信息的对话框的设计，文件名为*LookInfoDlg.py*，代码之中不包含对于按钮事件的响应

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LookInfoDlg.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(382, 140)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(50, 80, 301, 32))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lb_info = QtWidgets.QLabel(Dialog)
        self.lb_info.setGeometry(QtCore.QRect(40, 40, 55, 20))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.lb_info.setFont(font)
        self.lb_info.setObjectName("lb_info")
        self.lb_text = QtWidgets.QLabel(Dialog)
        self.lb_text.setGeometry(QtCore.QRect(110, 40, 240, 20))
        font = QtGui.QFont()
        font.setFamily("小米兰亭")
        self.lb_text.setFont(font)
        self.lb_text.setText("")
        self.lb_text.setObjectName("lb_text")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_info.setText(_translate("Dialog", "信息："))
```

显示效果如图
![showinfo](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_showinfo.jpg)

控制运行的*QtCommand.py*，其作用是创建窗口，显示窗口，而我们真正想要处理的按钮等的事件，已经在*HelloQtCommand.py*文件之中处理过了，主要是信号和槽函数的连接，以及槽函数对于具体情况的处理。

```python
# -*- coding: utf-8 -*-

import sys
import mypyqt5.HelloQtCommand as HelloQtCommand
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelloQtCommand.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
```

显示效果如图

![showeffect](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_showeffect.jpg)



##### 界面和逻辑分离
从以上可以看出，虽然我们可以对事件做出响应，但是其和界面文件混合在一起，如果我们需要修改其中的属性，就很有可能造成**逻辑和UI的混乱**，因此，有必要将逻辑和UI进行分离

逻辑和UI分离，主要有两种方式，一种是使用**函数的方式**，这一种不太面向对象，第二种是采用**类继承的方式**，这种比较常用。

下面通过案例来说明，如下文件为*speUI.py*，是界面文件，其中不包含槽函数和信号的连接以及槽函数的处理情况

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # self.inputSpinBox1 = QtWidgets.QSpinBox(Form)
        # self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        # self.inputSpinBox1.setObjectName("inputSpinBox1")  # 必须

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(321, 280)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 258, 225))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton.raise_()
        self.textBrowser.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 321, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "点我"))
```

显示效果如图
![dessep](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_dessep.jpg)

1.使用函数
使用函数的方式控制界面和逻辑分离，*usefunction.py*，其主要的思想是，在运行之前，**1.引入界面文件**，**2.再将其初始化**，**3.然后再关联信号和槽函数**，**4.实现槽函数，处理相应的情况**

```python
# -*- coding: utf-8 -*-

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
```

2.使用类继承
使用类继承的方式控制界面和逻辑分离，*usefunction.py*，**主要的思想是将设计好的ui文件转化生成的类文件，作为基类，然后新建一个类继承此基类，再在此子类之中对其进行信号和槽函数的关联，以及槽函数的处理**，如果将执行代码单独设置一个文件，则就是完全的界面和逻辑分离了。*其实这种方式也未必完全算是分离，但是如果没有一定程度的耦合，那么软件的功能也将无从实现*，**我们所说的分离，主要是指，设计的ui在一定程度上保持独立性，更改此模块不会对其他模块造成很大的影响**。

```python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QApplication

from pyqt2nd import speUI
from PyQt5 import QtCore, QtWidgets, QtGui

#  使用类继承的方式，来完成界面和逻辑的分离

class NewWindow(QtWidgets.QMainWindow, speUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_string)  # 信号

    def show_string(self):  # 槽函数
        str1 = self.lineEdit.text()
        self.textBrowser.setText(str1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = NewWindow()
    myshow.show()
    sys.exit(app.exec_())

    #  NoAttribuate问题的解决，主要是因为Qt Designer设计的APP,继承于QMainWindow而非QWidget
    #  https://stackoverflow.com/questions/43260595/attributeerror-ui-mainwindow-object-has-no-attribute-setcentralwidget-pyqt5
```

显示效果如图
![realeffect](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_realeffect.gif)



##### 类扩展方式的变换
类扩展的方式，由于python语言本身对于同一个功能可能有多种实现的方式，所以会有一些变种，但是其功能是相同的，只是代码书写的方式有些差异而已，如下是一个简易计算器的界面文件，*calc_ui.py*，其ui和逻辑是分离的

```python
# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calc(object):
    def setupUi(self, Form):
        self.inputSpinBox1 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox1.setGeometry(QtCore.QRect(1, 26, 46, 25))
        self.inputSpinBox1.setObjectName("inputSpinBox1")  # 必须

        self.inputSpinBox2 = QtWidgets.QSpinBox(Form)
        self.inputSpinBox2.setGeometry(QtCore.QRect(70, 26, 46, 25))
        self.inputSpinBox2.setObjectName("inputSpinBox2")  # 必须

        self.outputWidget = QtWidgets.QLabel(Form)
        self.outputWidget.setGeometry(QtCore.QRect(140, 24, 36, 27))
        self.outputWidget.setObjectName("outputWidget")  # 必须

        QtCore.QMetaObject.connectSlotsByName(Form)  # 必须

```

如下是逻辑控制部分的代码*calc.py*，实现了一个简易的加法计算器，界面和ui是分离的

```python
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
    # win = MyCalc2(
    win = MyCalc3()
    win.show()
    sys.exit(app.exec_())

    # https://www.cnblogs.com/hhh5460/p/5390999.html
    # http://blog.csdn.net/mr_zing/article/details/46945011

```

显示效果如图
![add](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_add.gif)

以上的三种方式功能是相同的，第一种和第二种方式，在槽函数和信号的处理中采用的是注解的方式（后续研究），明显要比第三种首先连接信号和槽函数，然后实现槽函数的这种方式简便很多，需要注意的是，此处*calc_ui.py*是手动方式写的，而我们直接使用*Qt Desginer*设计然后生成的这种方式，所继承的界面类可能不一样，==*手写的时候，还可以继承QWidget，而使用Qt Desginer的时候，继承的类是QMainWindow，虽然此两个类，都是继承于QtWidgets，但是具体的attribute是有差别的，如果不加以区分，则会产生"No XXXattribute的错误，如QtWidgets, QMainWindow, QDialog等*==，所以要在这个地方看清楚，以免发生*XXX has no attribute*的错误。**而且，在Qt之中，高级的模块包，都是用QtXXX来命名，而其下的子类则使用QXXX来命名，如QtWidgets和其子类QtWidgets。QMainWindow和QtWidgets.QWidget**。尤其要注意，使用*Qt Desginer*设计转化生成的ui类别，都是继承*QtWidgets.QMainWindow*, 所以我们在继承的时候，也都必须要以此类作为第一位置参数，将所要继承的类作为后续的参数，同时，也要注意**MRO**问题。



ref:
1.[pyqt5界面与逻辑分离--信号槽的装饰器实现方式](http://www.cnblogs.com/hhh5460/p/5390999.html),   2.[PyQt5学习笔记06----Qt Designer自定义信号emit及传参](http://blog.csdn.net/a359680405/article/details/45150569),   3.[[AttributeError: 'Ui_MainWindow' object has no attribute 'setCentralWidget' PyQt5](https://stackoverflow.com/questions/43260595/attributeerror-ui-mainwindow-object-has-no-attribute-setcentralwidget-pyqt5)](https://stackoverflow.com/questions/43260595/attributeerror-ui-mainwindow-object-has-no-attribute-setcentralwidget-pyqt5),   4.[PyQt5开发中如何让逻辑和界面分离](http://www.jianshu.com/p/6ad567c2fdc1)