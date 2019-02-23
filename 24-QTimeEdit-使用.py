# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeEdit")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        te=QTimeEdit(QTime.currentTime(),self)
        te.setDisplayFormat("hh=m-ss:zzz a")
        print(te.time())



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())