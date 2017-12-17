# -*- coding:utf-8-*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from pyqt2nd import TableUi, InfoDlg


class TableUiOpt(QtWidgets.QMainWindow, TableUi.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)
        self.inittable()

        self.addaction.triggered.connect(self.addtablerow)  # 添加一行
        self.deleteaction.triggered.connect(self.deletetablerow)  # 删除一行
        self.additemaction.triggered.connect(self.edittablerow)  # 编辑一行

    # 在此处去初始化table的行和列，而不去在UI转换的文件之中操作，这样方便操作
    def inittable(self):
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(5)
        mlabel = ['序号', '姓名', '年龄', '性别', '电话', '备注']
        self.tableWidget.setHorizontalHeaderLabels(mlabel)  # 设置表头

    def addtablerow(self):
        row1 = self.tableWidget.rowCount()
        print(row1)
        self.tableWidget.insertRow(row1)  # 动态增加行的时候，不需要减1

    def deletetablerow(self):
        row2 = self.tableWidget.rowCount()
        if row2 > 1:
            print(row2)
            self.tableWidget.removeRow(row2 - 1)  # 动态删除行的时候，需要减1

    # def edittablerow(self):  # 自己添加数据
    #     rowindex = 0
    #     columninex = 0
    #     if self.tableWidget.selectedItems() is None:
    #         rowindex = 0
    #         columninex = 0
    #     else:
    #         rowindex = self.tableWidget.currentRow()
    #         columninex = self.tableWidget.currentColumn()
    #         self.tableWidget.setItem(rowindex, columninex, QTableWidgetItem("001"))

    def edittablerow(self):  # 弹出dlg
        dlg = MyDialog()
        dlg.show()
        dlg.exec_()


class MyDialog(QtWidgets.QDialog, InfoDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initdlg()
        self.pushBtnCancle.clicked.connect(self.clearEdit)
        self.pushBtnOkay.clicked.connect(self.insertTableRow)

    def initdlg(self):
        listgender = ("男", "女")
        self.comboBoxAge.addItems(listgender)
        # 也可以使用additem
        # self.comboBoxAge.addItem("男")

    def clearEdit(self):
        self.lineEdNo.setText("")
        self.lineEdName.setText("")
        self.lineEdAge.setText("")
        self.lineEdPhone.setText("")
        self.textEdOtherinfo.setText("")

    # 一次只能输入一个cell，如何依次输入多个cell?
    # 可以一次添加多个cell，之前是因为没有找到对应的函数
    def insertTableRow(self):
        lineedno = self.lineEdNo.text().strip()
        lineedname = self.lineEdName.text().strip()
        lineedage = self.lineEdAge.text().strip()
        comboboxage = self.comboBoxAge.currentText().strip()
        lineedphone = self.lineEdPhone.text().strip()
        # lineedotherinfo = self.textEdOtherinfo.content
        # if (lineedno == "" | lineedname == "" | lineedage == "" | comboboxage == "" |
        #         lineedphone == "" | lineedotherinfo):
        #     return 0
        rowindex = 0
        if tableuiopt.tableWidget.selectedItems() is None:
            rowindex = 0
        else:
            rowindex = tableuiopt.tableWidget.currentRow()
            print(rowindex)
            tableuiopt.tableWidget.setItem(rowindex, 0, QTableWidgetItem(lineedno))
            tableuiopt.tableWidget.setItem(rowindex, 1, QTableWidgetItem(lineedname))
            # tableuiopt.tableWidget.setItem(rowindex, 2, QTableWidgetItem("123"))
            # tableuiopt.tableWidget.setItem(rowindex, 3, QTableWidgetItem("123"))
            # tableuiopt.tableWidget.setItem(rowindex, 4, QTableWidgetItem("123"))
            # tableuiopt.tableWidget.setItem(rowindex, 5, QTableWidgetItem("123"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableuiopt = TableUiOpt()
    # tableuiopt.inittable() #此处初始化也可以，但是不太规范
    tableuiopt.show()
    sys.exit(app.exec_())
