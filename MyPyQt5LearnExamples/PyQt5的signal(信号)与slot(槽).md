### PyQt5的signal(信号)与slot(槽)

***

**信号是对象发出来的，槽是一个处理函数，信号发射出来后，连接到相应的槽函数，就能对UI事件进行处理**。信号和槽是用来在对象间传递数据的方法：当一个特定事件发生的时候，signal会被emit出来，slot调用是用来响应相应的signal的。Qt中对象已经包含了许多预定义的 signal（基本组件都有各自特有的预定义的信号），根据使用的场景我们可以添加新的signal。Qt的对象中已经包含了许多预定义的槽函数，但我们也根据使用的场景添加新的槽函数

##### signal(信号)
*当对象的状态发生改变的时候*，**`信号`就由该对象发射 (emit) 出去**。当一个信号被发射(emit)时候，++与其关联的`==槽函数==`被立刻执行++。其中该对象只负责发送信号，发射该信号的对象并不知道是那个对象在接收这个信号。这样保证了对象与对象之间的低耦合。

也就是说，信号是对象状态改变时候发出的，**信号对应的的主体是对象**，比如一个button，Qt为我们准备了很多的内置信号，比如最常用的**clicked**，就是一个信号，我们是使用信号"📶"来关联slot槽函数的。

**如果存在信号和多个槽函数相关联的时候，当信号被发射时，这些槽的执行顺序将会是随机的、不确定的**。



##### slot(槽)
用于接受信号，而且槽只是普通的对象成员函数。当和槽连接的信号被发射时，槽会被调用。一个槽并不知道是否有任何信号与自己相连接。



#####信号和槽的绑定
通过调用 QObject 对象的**connect**函数来将*某个对象的信号*与另外一个对象的槽函数相关联，这样当发射者发射信号时，接收者的槽函数将被调用。该函数的定义如下

> connect(slot[, type=PyQt5.QtCore.Qt.AutoConnection[, no_receiver_check=False]])
>
> Parameters:
>
> **slot** – the slot to connect to, either a Python callable or another bound signal.
>
> **type** – the type of the connection to make.
>
> **no_receiver_check** – suppress the check that the underlying C++ receiver instance still exists and deliver the signal anyway

当信号与槽没有必要继续保持关联时，我们可以使用 disconnect 函数来断开连接。其定义如下

> disconnect([slot])
>
> Parameters:
>
> **slot** – the optional slot to disconnect from, either a Python callable or another bound signal. If it is omitted then all slots connected to the signal are disconnected.



#####信号和槽的特点
1️⃣.**一个信号可以连接到多个槽**
​    当信号发出后，槽函数都会被调用，但是调用的顺序是随机的，不确定的。

```python
self.slider.valueChanged.connect(self.pBar.setValue)
self.slider.valueChanged.connect(self.lcdNumber.display)1
```

QSlider数据的变化同时绑定在setValue()和display()两个槽上。

2️⃣.**多个信号可以连接到同一个槽**
​    其中任何一个信号发出，槽函数都会被执行

```python
self.buttonOn.clicked.connect(self.showMessage)
self.buttonOff.clicked.connect(self.showMessage)
```

showMessage()同时绑定在两个button的clicked信号上。

3️⃣.**信号可以和另外一个信号进行关联**
​    第一个信号发出后，第二个信号也同时发送。比如关闭系统的信号发出之后，同时会发出保存数据的信号

4️⃣.信号和槽的连接可以被移除 
​    比如断开某个特定信号的关联。

```python
self.buttonOn.clicked.connect(self.showMessage)
```

5️⃣.信号的参数可以是任何的Python类型
​    如list，dict等python独有的类型。自定义信号的时候举例说明



##### 自定义信号
PyQt5已经自动定义了很多QT内建的信号。但是在实际的使用中为了灵活使用信号与槽机制，我们可以根据需要自定义signal。可以使用pyqtSignal()方法定义新的信号，新的信号作为类的属性。

*自定义signal说明*

pyqtSignal()方法原型（PyQt官网的定义）：

```python
PyQt5.QtCore.pyqtSignal(types[, name[, revision=0[, arguments=[]]]])
Create one or more overloaded unbound signals as a class attribute.

Parameters: 
types – the types that define the C++ signature of the signal. Each type may be a Python type object or a string that is the name of a C++ type. Alternatively each may be a sequence of type arguments. In this case each sequence defines the signature of a different signal overload. The first overload will be the default.

name – the name of the signal. If it is omitted then the name of the class attribute is used. This may only be given as a keyword argument.

revision – the revision of the signal that is exported to QML. This may only be given as a keyword argument.

arguments – the sequence of the names of the signal’s arguments that is exported to QML. This may only be given as a keyword argument.
Return type:    an unbound signal123456789101112
```

新的信号应该定义在QObject的子类中。新的信号必须作为定义类的一部分，不允许将信号作为类的属性在类定义之后通过动态的方式进行添加。通过这种方式新的信号才能自动的添加到QMetaObject类中。这就意味这新定义的信号将会出现在Qt Designer，并且可以通过QMetaObject API实现内省。 
通过下面的例子，了解一下关于signal的定义：

```python
from PyQt5.QtCore import QObject, pyqtSignal

class NewSignal(QObject):

    # 定义了一个“closed”信号，该信号没有参数据
    closed= pyqtSignal()

    # 定义了一个"range_changed"信号，该信号有两个int类型的参数
    range_changed = pyqtSignal(int, int, name='rangeChanged')
12345678910
```

------

自定义信号的发射，通过emit()方法类实现，具体参见该函数的原型：

```python
emit(*args)
Parameters: args – the optional sequence of arguments to pass to any connected slots.12
```

通过下面的例子，了解一下关于emit()的使用：

```python
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
1234567891011121314151617
```



#####示例说明

自定义信号的一般流程如下：
1、定义信号
2、定义槽函数
3、绑定信号和槽
4、发射信号

通过代码示例来了解一下信号的自定义过程：

```python
#-*- coding:utf-8 -*-
'''
defined Signal
'''
__author__ = 'Tony Zhu'
import sys
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QCheckBox, QSpinBox, QHBoxLayout, QComboBox, QGridLayout


class SignalEmit(QWidget):
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    #声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int,str],[str])
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
        self.previewSignal[int,str].connect(self.previewPaperWithArgs)
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('defined signal')
        self.show()

    def creatContorls(self,title):
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("打印")
        self.previewButton  = QPushButton("预览")
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

    def creatResult(self,title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)

    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int,str].emit(1080," Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")

    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value ())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self,list):
        self.resultLabel.setText("Print: "+"份数："+ str(list[0]) +"  纸张："+str(list[1]))

    def previewPaperWithArgs(self,style,text):
        self.resultLabel.setText(str(style)+text)

    def previewPaper(self,text):
        self.resultLabel.setText(text)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    def showHelpMessage(self,message):
        self.resultLabel.setText(message)
        #self.statusBar().showMessage(message)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())
```

运行该函数之后的效果如下
![这里写图片描述](http://images.cnblogs.com/cnblogs_com/prayjourney/1041349/o_jiemian.jpg)

**示例说明：**
通过一个模拟打印的界面来详细说明一下关于信号的自定义，在打印的时候可以设定打印的分数，纸张类型，触发“打印”按钮之后，将执行结果显示到右侧；通过全屏预览QCheckBox来选择是否通过全屏模式进行预览，将执行结果显示到右侧。 
通过点击F1快捷键，可以显示helpMessage信息。 
**代码分析：**
L12~15：

```python
    helpSignal = pyqtSignal(str)
    printSignal = pyqtSignal(list)
    #声明一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及带str参数的信号
    previewSignal = pyqtSignal([int,str],[str])1234
```

通过pyqtSignal()定义了三个信号，helpSignal ，printSignal ，previewSignal 。其中
helpSignal 为str参数类型的信号；
printSignal 为list参数类型的信号；
previewSignal为一个多重载版本的信号，包括了一个带int和str类型参数的信号，以及str类行的参数。

L31~36：

```python
self.helpSignal.connect(self.showHelpMessage)
self.printSignal.connect(self.printPaper)
self.previewSignal[str].connect(self.previewPaper)        self.previewSignal[int,str].connect(self.previewPaperWithArgs)         self.printButton.clicked.connect(self.emitPrintSignal)        self.previewButton.clicked.connect(self.emitPreviewSignal)123
```

绑定信号和槽；着重说明一下多重载版本的信号的绑定，previewSignal有两个版本previewSignal(str)，previewSignal(int,str)。由于存在两个版本，从因此在绑定的时候需要显式的指定信号和槽的绑定关系。

具体如下：
self.previewSignal[str].connect(self.previewPaper) self.previewSignal[int,str].connect(self.previewPaperWithArgs)
其中[str]参数的previewSignal信号绑定previewPaper();[int,str]的previewSignal信号绑定previewPaperWithArgs()

L72~76:

```python
    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() == True:
            self.previewSignal[int,str].emit(1080," Full Screen")
        elif self.previewStatus.isChecked() == False:
            self.previewSignal[str].emit("Preview")12345
```

多重载版本的信号的发射也需要制定对应发射的版本，类似同信号的版定。

L78~82：

```python
    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value ())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)12345
```

如代码中所示，在信号发射的时候可以传递python数据类型的参数，在本例中传递list类型的参数pList.

L93~96：

```python
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")123
```

通过复写keyPressEvent()方法，将F1快捷键进行功能的拓展。在windows的大部分应用，我们都会使用一些快捷键来快速的完成某些特定的功能。比如F1键，会快速调出帮助界面。那我们就可以复写keyPressEvent()方法来模拟发送所需的信号，来完成我们的对应任务



#####注意事项

1.自定义的信号在**init**()函数之前定义； 
2.自定义型号可以传递，str、int、list、object、float、tuple、dict等很多类型的参数； 
3.注意signal和slot的调用逻辑，避免signal和slot之间出现死循环。如在slot方法中继续发射该信号；

ref:

1.[PyQt5学习笔记05----Qt Designer信号槽](http://blog.csdn.net/a359680405/article/details/45148717),  2.[PyQt5学习笔记06----Qt Designer自定义信号emit及传参](http://blog.csdn.net/a359680405/article/details/45150569),  3.[PyQt之玩转signal(信号)与slot(槽)一：介绍及简单实例](http://blog.csdn.net/u011943221/article/details/47006549),  4.[**Pyqt5系列(七)-信号与槽机制**](http://blog.csdn.net/zhulove86/article/details/52530214),  5.[**Pyqt5系列(八)-自定义信号**](http://blog.csdn.net/zhulove86/article/details/52563131)