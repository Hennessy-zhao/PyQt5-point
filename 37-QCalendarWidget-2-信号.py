# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cw=QCalendarWidget(self)

        # cw.activated.connect(lambda date:print(date))         #按回车才会触发
        # cw.clicked.connect(lambda date:print(date))
        # cw.currentPageChanged.connect(lambda y,d:print(y,d))
        cw.selectionChanged.connect(lambda :print("选中的日期发生改变",cw.selectedDate()))       #如果一开始就设定了日期，则也会触发该信号


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())