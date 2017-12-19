### PyQt5创建和引用Resource文件

***

##### 创建和引用Resource文件

创建Resource文件有两种方式，一种是**手动创建**，一种是通过**Qt Designer创建**，引用的方式无太多差异

手动创建时，在`Pycharm`等`IDE`之中，添加好`.qrc`文件，然后通过配置在External Tool中的`Pyrcc`来将资源文件转化成python文件，然后在需要的地方引用，在引用的时候，需要将转化后的python文件导入到引用的文件之中。由于我们可能需要创建多个Resource文件，所以可以将`.qrc`文件创建一个模版，只需要在其中添加file的路径即可

![configtemplate](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_configtemplate.jpg)

添加好之后，可以直接创建，显示如下

![configshow](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_configshow.jpg)

通过Qt Designer创建时，首先需要通过File-> Tools-> External tools启动Qt Designer，然后在创建好我们需要的窗口、对话框等资源之后，在属性之中设置其引用的图标或者资源或者主题，选择资源创建资源，然后即可创建资源或者从已有的资源之中为控件添加图标等

![desgineresource](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_desgineresource.jpg)

引用的部分，第一种方法和第二种方法相同，资源设计完成，引用正确时，显示如下图图标

![showicon](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_showicon.jpg)



##### 转换资源文件

把`.qrc`资源文件转换成十六进制的py文件，右键工程目录 resource.qrc，External tools 点击pyrcc.
目录下生成资源对应的resource.py

![transferresource](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_transferresource.jpg)



##### 例子

资源文件`res2.qrc`

```xml
<RCC>
    <qresource prefix="newPrefix">
        <file>image/app.png</file>
        <file>image/snow.ico</file>
        <file>image/mnv.jpg</file>
    </qresource>
</RCC>
```

UI文件`ResourceUse.py`

```python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResourceUse.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt2nd import res2_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 319)
        # 此处是在Qt Desginer之中生成的，开发的时候最好不要在此处弄，可以在继承类之中二次初始化完成
        # icon = QtGui.QIcon()
        # icon.addPixmap(QtGui.QPixmap(":/newPrefix/image/app.png"))
        # MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "使用资源文件"))

```

控制文件`FirstResource.py`

```python
from PyQt5 import QtWidgets, QtGui
import sys

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QWindow, QIcon, QPixmap, QPalette, QBrush
from PyQt5.QtWidgets import QApplication
from pyqt2nd import ResourceUse
from pyqt2nd import res2_rc  # 需要导入，不然显示有问题


class FirstResource(QtWidgets.QMainWindow, ResourceUse.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.secondinit()

    # 通过资源文件自定义的设置图标
    def secondinit(self):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/image/snow.ico"))
        self.setWindowIcon(icon)
        # 设置窗口背景
        pixmap = QPixmap(":/newPrefix/image/mnv.jpg").scaled(self.size())  # 适应窗口大小
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(pixmap))
        self.setPalette(palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    useresource = FirstResource()
    useresource.show()
    sys.exit(app.exec_())

```

显示效果

![resourceuseshow](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_resourceuseshow.jpg)

ref:

1.[pyqt 加载资源文件](http://blog.csdn.net/jxm_csdn/article/details/51815794),   2.[PyQt5简易入门指南03，使用资源文件和设计师](http://blog.csdn.net/linuxlike/article/details/76099983)

