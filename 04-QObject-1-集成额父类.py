# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject的学习")
        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()


    #QObject继承结构测试
    def test_QObject(self):
        mors=QObject.mro()      #获取QObject的父类

        for mro in mors:
            print(mro)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())