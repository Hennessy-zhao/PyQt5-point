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
        # cw.setSelectedDate(QDate(-9999,1,1))
        cw.setMinimumDate(QDate(1990,1,1))
        cw.setMaximumDate(QDate(2020,12,12))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())