# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("UI的学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        from PyQt5.uic import loadUi
        loadUi("class_ts.ui", self)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    def click():
        print("xxx")
        account=form.lineEdit.text()
        pwd=form.lineEdit_2.text()
        print(account,pwd)
    form.pushButton.clicked.connect(click)

    sys.exit(app.exec_())