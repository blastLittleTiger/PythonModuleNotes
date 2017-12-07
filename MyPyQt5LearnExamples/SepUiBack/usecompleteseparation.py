# -------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# 完全的界面分离

import sys
from PyQt5.QtWidgets import QWidget, QApplication

from pyqt2nd.useclass import NewWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = NewWindow()
    myshow.show()
    sys.exit(app.exec_())
