### PyQt5基本模块的作用

***

#####  基本模块的作用
PyQt5是一套来自Digia的Qt5应用框架和Python的粘合剂。支持Python2.x和Python3.x版本。

PyQt5以一套Python模块的形式来实现功能。它包含了超过620个类，600个方法和函数。它是一个多平台的工具套件，它可以运行在所有的主流操作系统中，包含Unix，Windows和Mac OS。PyQt5采用双重许可模式。开发者可以在GPL和社区授权之间选择。

QtWidgets在PyQt5之中从QtGui模块之中分离出来了，**QtWidgets**专注的是传统UI界面的构建，而构建现代的，动态的，有各种动态效果的Gui则是使用**QtQuick**，和**QtQuickWidgets**，需要注意的一点是，在高级别的PyQt组件之中，API 的命名是QtCore，QtGui，QtWidgets是以"**Qt**"作为开头，构成QtXXX的模式的，而在这些组件下的子组件，则是使用**Q**开头，构成QXXX的模式，如QMainWindow和QWidget，其实这两个子类，都是在QtWidgets之下的。

PyQt5的类被划分在几个模块中，下面列出了这些模块：

- **QtCore** : 模块包含了非GUI的功能设计。这个模块被用来实现时间，文件和目录，不同数据类型，流，URL，mime类型，线程和进程。
- **QtGui** : 模块包含的类用于窗口化的系统结构，事件处理，2D绘图，基本图形，字体和文本。
- **QtWidgets** : 模块包含的类提供了一套UI元素来创建经典桌面风格用户界面。
- QtMultimedia：模块包含的类用于处理多媒体内容和链接摄像头和无线电功能的API。
- QtBluetooth：模块包含的类用于扫描蓝牙设备，并且和他们建立连接互动。
- QtNetwork：模块包含的类用于网络编程，这些类使TCP/IP和UDP客户端/服务端编程更加容易和轻便。
- QtPositioning：模块包含的类用于多种可获得资源的位置限定，包含卫星定位，Wi-Fi，或一个文本文件。
- Enginio：模块用于解决客户端访问Qt云服务托管。
- QtWebSockets：模块用于解决客户端访问Qt云服务托管。
- QtWebKit：包含的关于浏览器的类用于解决基于WebKit2的支持库。
- QtWebKitWidgets：模块包含的关于WebKit1的类基本解决浏览器使用基于QtWidgets应用问题。 
- QtXml：`QtXml` 模块包含的类用于解析XML文件。这个模块提供SAX和DOM API解决方法。
- QtSvg：模块提供类用于显示SVG文件内容。Scalable Vector Graphics (SVG) 是一种语言，用XML来描述二维图形和图形应用程序。
- QtSql：模块提供类驱动数据库工作。 
- QtTest：模块包含了方法提供PyQt5应用的单元测试。



##### PyQt5和PyQt4
PyQt5不向后兼容PyQt4；这是一些在PyQt5中的重要改变。然而，将旧代码迁移到新的版本中并不是非常困难。不同点如下：

- Python 模块已经被改写. 一些模块被舍弃 (`QtScript`), 部分的模块被分割成子模块 (`QtGui`, `QtWebKit`).
- 新的模块被引进, 包含 `QtBluetooth`, `QtPositioning`, 和 `Enginio`.
- PyQt5 只支持最新风格的信号和槽的写法. SIGNAL()和SLOT()的调用将不会被长时间支持.
- PyQt5 不支持任何在Qt 5.0版本中弃用或取消的API.

ref:

1.[pyqt5-基础](http://www.cnblogs.com/qjoanven/p/7843701.html),   2.[对比分析:Qt中的用户界面](http://qiusuoge.com/12754.html),   3.[Python电子书 教程](https://zhuanlan.zhihu.com/p/26294285)