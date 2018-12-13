# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("对象的父子关系")

        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_QObject(self):
        object0=QObject()
        object1=QObject()
        object2=QObject()
        object3=QObject()
        object4=QObject()
        object5=QObject()

        print("QObject0:",object0)
        print("QObject1:",object1)
        print("QObject2:",object2)
        print("QObject3:",object3)
        print("QObject4:",object4)
        print("QObject5:",object5)

        object1.setParent(object0)
        object2.setParent(object0)
        object3.setParent(object1)
        object4.setParent(object2)
        object5.setParent(object2)

        print(object1.parent())
        print(object2.children())
        print(object2.findChildren(QObject))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())