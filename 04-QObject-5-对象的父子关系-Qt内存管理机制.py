# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")

        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_QObject(self):
        obj1=QObject()
        obj2=QObject()

        obj2.setParent(obj1)

        #监听obj2对象被释放
        obj2.destroyed.connect(lambda :print("obj2对象被释放了"))     #父对象被删除，子对象也会被删除

        del obj1



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())