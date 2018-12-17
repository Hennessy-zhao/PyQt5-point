# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyAgeVaditator(QIntValidator):
    def fixup(self, p_str):
        print("xxx",p_str)
        if len(p_str)==0 or int(p_str)<18:
            return "18"

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        le=QLineEdit(self)
        le.move(100,100)
        vaditator=MyAgeVaditator(18,180)     #限制是18-180
        le.setValidator(vaditator)

        le1 = QLineEdit(self)
        le1.move(100, 200)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())