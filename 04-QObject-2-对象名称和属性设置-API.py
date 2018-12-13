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


    #QObject对象名称和属性操作
    def test_QObject(self):
        obj=QObject()
        obj.setObjectName("obj1")
        print(obj.objectName())

        obj.setProperty("obj_level1","error")
        obj.setProperty("obj_level2","warning")

        print(obj.property("obj_level1"))

        print(obj.dynamicPropertyNames())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())