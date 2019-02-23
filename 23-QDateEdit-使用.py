# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateEdit")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        de=QDateEdit(self)
        de.setDisplayFormat("yy-MMMM-dddd")
        print(de.date())



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())