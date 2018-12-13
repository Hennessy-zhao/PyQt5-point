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
        self.test_QObjeect()

    def test_QObjeect(self):
        obj1=QObject()
        self.obj1=obj1
        obj2=QObject()
        obj3=QObject()

        obj3.setParent(obj2)
        obj2.setParent(obj1)

        obj1.destroyed.connect(lambda: print("obj1被释放了"))
        obj2.destroyed.connect(lambda: print("obj2被释放了"))
        obj3.destroyed.connect(lambda: print("obj3被释放了"))

        # del obj2      #真正的对象没有被杀掉，只是断开了联系。但是真正的obj2还在被window所引用折

        obj2.deleteLater()      #删除对象  并没有立刻销毁对象后面才会真正的释放对象

        print(obj1.children())


if __name__=='__main__':
    app=QApplication(sys.argv)
    window=Demo()
    window.show()
    sys.exit(app.exec_())
