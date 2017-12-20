# -*- coding:utf-8-*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QFont
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqt2nd import TableUi, InfoDlg, tableuires_rc

_author = "游侠最光阴"  # 设置作者
_version = "V0.9.8"  # 设置版本号


class TableUiOpt(QtWidgets.QMainWindow, TableUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.init_table()

        # 菜单菜单列表
        self.addaction.triggered.connect(self.add_table_row)  # 添加一行
        self.deleteaction.triggered.connect(self.delete_table_row)  # 删除一行

        # 内容菜单列表
        self.additemaction.triggered.connect(self.insert_row)  # 编辑一行
        self.updateitemaction.triggered.connect(self.update_row)  # 更新一行
        self.updateitemaction.triggered.connect(self.delete_row)  # 删除一行

        # 说明菜单列表
        self.declareaction.triggered.connect(self.show_declaration)  # 显示声明

    # 在此处去初始化table的行和列，而不去在UI转换的文件之中操作，这样方便操作
    def init_table(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)
        mlabel = ['序号', '姓名', '年龄', '性别', '电话', '备注']
        self.tableWidget.setHorizontalHeaderLabels(mlabel)  # 设置表头
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置双击不编辑
        self.tableWidget.setAlternatingRowColors(True)  # 改变正在修改的行的颜色
        # 如何给某一个cell设置tooltip?
        # 设置表格的颜色
        for index in range(self.tableWidget.columnCount()):
            headItem = self.tableWidget.horizontalHeaderItem(index)
            headItem.setFont(QFont("微软雅黑", 10, QFont.Bold))  # 设置字体
            headItem.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)  # 设置
            if (index % 2 == 0):
                headItem.setBackground(QBrush(Qt.blue))  # 设置背景，但好像没有用
            else:
                headItem.setForeground(QBrush(Qt.darkCyan))
        # 单独设置背景颜色，无法起作用？
        self.tableWidget.horizontalHeaderItem(2).setForeground(QBrush(Qt.green))

        # 设置主界面的图标
        icon_app = QtGui.QIcon()
        icon_app.addPixmap(QtGui.QPixmap(":/myres/img123/app9.png"))
        self.setWindowIcon(icon_app)
        icon_add_row = QtGui.QIcon()
        icon_add_row.addPixmap(QtGui.QPixmap(":/myres/img123/add9.png"))
        self.addaction.setIcon(icon_add_row)
        icon_delete_row = QtGui.QIcon()
        icon_delete_row.addPixmap(QtGui.QPixmap(":/myres/img123/sub9.png"))
        self.deleteaction.setIcon(icon_delete_row)
        icon_add_item = QtGui.QIcon()
        icon_add_item.addPixmap(QtGui.QPixmap(":/myres/img123/addcir9.png"))
        self.additemaction.setIcon(icon_add_item)
        icon_update_item = QtGui.QIcon()
        icon_update_item.addPixmap(QtGui.QPixmap(":/myres/img123/edit9.png"))
        self.updateitemaction.setIcon(icon_update_item)
        icon_delete_item = QtGui.QIcon()
        icon_delete_item.addPixmap(QtGui.QPixmap(":/myres/img123/subcir9.png"))
        self.deleteitemaction.setIcon(icon_delete_item)
        icon_save_to_db = QtGui.QIcon()
        icon_save_to_db.addPixmap(QtGui.QPixmap(":/myres/img123/save9.png"))
        self.savetodbaction.setIcon(icon_save_to_db)
        icon_excel = QtGui.QIcon()
        icon_excel.addPixmap(QtGui.QPixmap(":/myres/img123/excel9.png"))
        self.importfromexcelaction.setIcon(icon_excel)
        self.exporttoexcelaction.setIcon(icon_excel)
        icon_help = QtGui.QIcon()
        icon_help.addPixmap(QtGui.QPixmap(":/myres/img123/help9.png"))
        self.helpaction.setIcon(icon_help)
        icon_declare = QtGui.QIcon()
        icon_declare.addPixmap(QtGui.QPixmap(":/myres/img123/favor9.png"))
        self.declareaction.setIcon(icon_declare)

    def add_table_row(self):
        row1 = self.tableWidget.rowCount()
        print(row1)
        self.tableWidget.insertRow(row1)  # 动态增加行的时候，不需要减1

    def delete_table_row(self):
        row2 = self.tableWidget.rowCount()
        if row2 > 1:
            print(row2)
            self.tableWidget.removeRow(row2 - 1)  # 动态删除行的时候，需要减1

    def insert_row(self):  # 添加一行数据，弹出添加用户的dlg
        insertdlg = MyInsertDialog()
        insertdlg.show()
        insertdlg.exec_()

    def update_row(self):  # 更新一行数据
        updatedlg = MyUpdateDialog()
        updatedlg.show()
        updatedlg.exec_()

    def delete_row(self):  # 删除一行数据
        pass

    def show_declaration(self):
        QMessageBox.about(self, "关于", "版本:  " + _version + "\n" + "作者:  " + _author)


class MyInsertDialog(QtWidgets.QDialog, InfoDlg.Ui_Dialog):
    __title = "添加联系人信息"

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.second_init()
        self.pushBtnCancle.clicked.connect(self.clear_edit)
        self.pushBtnOkay.clicked.connect(self.insert_table_row)

    def second_init(self):
        self.setWindowTitle(self.__title)  # 设置了标题栏
        listgender = ("男", "女")
        self.comboBoxGender.addItems(listgender)
        self.setModal(True)  # 设置模态和非模态对话框
        # 也可以使用additem
        # self.comboBoxAge.addItem("男")
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap(":/myres/img123/addcir9.png"))
        self.setWindowIcon(window_icon)

    def clear_edit(self):
        self.lineEdNo.setText("")
        self.lineEdName.setText("")
        self.lineEdAge.setText("")
        self.lineEdPhone.setText("")
        self.textEdOtherinfo.setText("")

    # 一次只能输入一个cell，如何依次输入多个cell?
    # 可以一次添加多个cell，之前是因为没有找到对应的函数
    def insert_table_row(self):
        lineedno = self.lineEdNo.text().strip()
        lineedname = self.lineEdName.text().strip()
        lineedage = self.lineEdAge.text().strip()
        comboxgender = self.comboBoxGender.currentText().strip()
        lineedphone = self.lineEdPhone.text().strip()
        lineedotherinfo = self.textEdOtherinfo.toPlainText().strip()  # 获取文本内容
        # if (lineedno == "" | lineedname == "" | lineedage == "" | comboxgender == "" |
        #     lineedphone == "" | lineedotherinfo == ""):
        #     return 0
        rowindex = 0
        if tableuiopt.tableWidget.selectedItems() is None:
            rowindex = 0
        else:
            rowindex = tableuiopt.tableWidget.currentRow()
            print(rowindex)
            tableuiopt.tableWidget.setItem(rowindex, 0, QTableWidgetItem(lineedno))
            tableuiopt.tableWidget.setItem(rowindex, 1, QTableWidgetItem(lineedname))
            tableuiopt.tableWidget.setItem(rowindex, 2, QTableWidgetItem(lineedage))
            tableuiopt.tableWidget.setItem(rowindex, 3, QTableWidgetItem(comboxgender))
            tableuiopt.tableWidget.setItem(rowindex, 4, QTableWidgetItem(lineedphone))
            tableuiopt.tableWidget.setItem(rowindex, 5, QTableWidgetItem(lineedotherinfo))
        self.close()  # 添加了一个联系人，点击确定之后，自动关闭对话框


class MyUpdateDialog(QtWidgets.QDialog, InfoDlg.Ui_Dialog):
    __title = "更新联系人信息"

    def __init__(self, parent=None):
        super(MyUpdateDialog, self).__init__(parent)
        self.setupUi(self)
        self.second_init()

    def second_init(self):
        self.setWindowTitle(self.__title)
        window_icon = QtGui.QIcon()
        window_icon.addPixmap(QtGui.QPixmap(":/myres/img123/edit9.png"))
        self.setWindowIcon(window_icon)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableuiopt = TableUiOpt()
    # tableuiopt.inittable() #此处初始化也可以，但是不太规范
    tableuiopt.show()
    sys.exit(app.exec_())
