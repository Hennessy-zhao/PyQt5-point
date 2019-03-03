# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from class_ts import Ui_Form
import sys

class Demo(QWidget,Ui_Form):            #多继承
    def __init__(self):
        super().__init__()
        self.setWindowTitle("加载UI文件的学习")
        self.resize(500,500)

        self.setupUi(self)          #加载文件

    def setup_ui(self):
        pass

    def btn_click(self):
        print(self.lineEdit.text())
        print(self.lineEdit_2.text())

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()


    sys.exit(app.exec_())