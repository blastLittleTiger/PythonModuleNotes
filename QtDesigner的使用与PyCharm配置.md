###Qt Designer 设计师

***

#####安装PyQt5
官方网站：<http://www.riverbankcomputing.com/software/pyqt/download5>

我的操作系统是64位的，安装的是Python3.4.3，所以我选择下载：[PyQt5-5.4.1-gpl-Py3.4-Qt5.4.1-x64.exe](http://sourceforge.net/projects/pyqt/files/PyQt5/PyQt-5.4.1/PyQt5-5.4.1-gpl-Py3.4-Qt5.4.1-x64.exe/download)

单击安装即可。

PyQt5安装完后，需要修改系统变量

QT_QPA_PLATFORM_PLUGIN_PATH
C:\Python34\Lib\site-packages\PyQt5\plugins                                      <<-----------------这是我PyQt5的plugins文件夹所在位置

![img](http://img.blog.csdn.net/20150416164922007?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)




#####初识Qt Designer
打开PyQt5的Qt Designer，会自动弹出新建窗体对话框，对于我们最常用的就是Widget通用窗口类，还有个MainWindows顾名思义主窗口。PyQt5的Widget被分离出来，似乎用来替代Dialog，并将Widget放入了QtWidget模块（库）中，PyQt4是QtGUI。

![img](http://img.blog.csdn.net/20150417163156740?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

这是一个Widget和MainWindows，MainWindows默认添加了菜单栏、工具栏和状态栏等。默认左边是控件栏，提供了很多空间类，我们可以直接拖放到widget中看到效果，点窗体--预览（Ctrl+R）。每个空间都有自己的名称，提供不同的功能，比如常用的按钮、输入框、单选、文本框等等。右边是对窗口及控件的各种调整、设置、添加资源（列如:图片）、动作。还可以直接编辑Qt引以为豪的信号槽（signal和slot）。有了Qt Designer使得我们在程序设计中更快的能开发设计出程序界面，避免了用纯代码来写一个窗口的繁琐，同时PyQt支持界面与逻辑分离，这对于新手来说无疑是个最大的福音，当然要做出华丽的界面还是要学代码的。至少Qt Designer为我们提供了一些解决方法，另外我们也可以通过Qt Designer生成的代码来学习一些窗口控件的用法。

#####Qt Designer Layouts窗口布局

![img](http://img.blog.csdn.net/20150417170117468?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

Qt Designer窗口布局Layouts提供了四种布局方法，他们是：

Vertical Layout 纵向布局
Horizontal Layout 横向布局
Grid Layout  栅格布局
Form Layout  在窗体布局中布局

前三种是我们经常会用到的，我们将布局Layouts拖动到窗体上会有红色框来显示（中间窗体中的四个小红框就是），Layout的一些属性可以通过属性编辑器来控制，一般包括：上下左右边距间隔，空间之间间隔等。
在我们使用布局之前，我们得对层次要有个了解，在程序设计中一般用父子关系来表示。当然有过平面设计经验的童鞋对分层应该有所了解，这里我们还需要将层分成层次。其实就像python中规定的代码缩进量代表不同层次的道理差不多。

![img](http://img.blog.csdn.net/20150417170928785?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

从对象查看器中我们可以方便的看出窗体（Form）--布局（Layout）--控件（这里是PushButton按钮）之间的层次关系。Form窗口一般作为顶层显示，然后使用Layout将控件按照我们想要的方式规划开来。

**小提示**：

通常我们使用栅格布局作为顶层布局，将控件放置好之后可以通过右键--布局--栅格布局，将布局充满整个窗体。我们可以先放入控件，然后ctrl选中多个控件，然后点击工具栏上快速布局工具进行布局。

这里要注意一下，Qt Designer设计出来的文件默认为ui文件，里面包含的类css布局设计语言，如果想要查看代码我们还需要将它转换（编译）成py文件，我们可以使用一条DOS命令来完成D:\Python33\Lib\site-packages\PyQt5\pyuic5.bat main.ui -o frist.py。  我的pycharm经过[PyQt5+python3+pycharm开发环境配置（点击我）](http://blog.csdn.net/a359680405/article/details/45074761)的配置。通过下图的操作可以便捷的对UI进行转化

![img](http://img.blog.csdn.net/20150417171751137?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

更实用的转换命令可以将当前文件夹下所有ui转换成py文件：

for /f "delims=" %%i in ('dir /b /a-d /s *.ui') do D:\Python33\Lib\site-packages\PyQt5\pyuic5.bat %%i -o %%i.py

PyQt支持用LoadUi方法直接加载ui文件，当然我们通过转换后可以方便学习PyQt窗体控件的源代码。



#####配置PyCharm
1.打开PyCharm，执行快捷键ctrl+alt+s打开设置界面，输入tool，点开external tools，配置qtdesigner。

点击左上角的加号，作如下配置：

在Qt Designer的设置中，Program选择PyQt安装目录中 designer.exe 的路径

Work directory 使用变量 $FileDir$ （点击后面的 Insert macro 按钮可以不用输入双击上屏）

![img](http://img.blog.csdn.net/20150422140556771?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

2.设置“PyUIC” -- 这个主要是用来将 Qt界面 转换成 py代码

在PyUIC的设置中，其他的都差不多，Program 写入Python的地址，Parameters写入

> -m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py

把上面的Python路径修改成自己的即可！

Work directory 使用变量 $FileDir$

![img](http://img.blog.csdn.net/20150416143917298?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

使用时先用QtDesigner生成ui文件，然后利用PyUIC将ui文件转换成对应python文件

3.资源文件转码

最近用到了资源文件，资源文件需要用pyrcc5.exe转码，配置方式如图

![img](http://img.blog.csdn.net/20150422140631060?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvYTM1OTY4MDQwNQ==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)



ref:
1.[PyQt5学习笔记02----初探Qt Designer 设计师](http://blog.csdn.net/a359680405/article/details/45098695),   2.[PyQt5+python3+pycharm开发环境配置](http://blog.csdn.net/a359680405/article/details/45074761)