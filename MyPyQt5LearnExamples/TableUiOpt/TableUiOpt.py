# -*- coding:utf-8-*-
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from pyqt2nd import TableUi


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

    def edittablerow(self):  # 自己添加数据
        rowindex = 0
        columninex = 0
        if self.tableWidget.selectedItems() is None:
            rowindex = 0
            columninex = 0
        else:
            rowindex = self.tableWidget.currentRow()
            columninex = self.tableWidget.currentColumn()
            self.tableWidget.setItem(rowindex, columninex, QTableWidgetItem("001"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    tableuiopt = TableUiOpt()
    # tableuiopt.inittable() #此处初始化也可以，但是不太规范
    tableuiopt.show()
    sys.exit(app.exec_())
