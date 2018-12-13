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
        obj=QObject()
        w=QWidget()
        btn=QPushButton()
        label=QLabel()

        objs=[obj,w,btn,label]
        for o in objs:
            #print(o.isWidgetType())         #判断对象是不是控件类别
            print(o.inherits("QPushButton"))    #判断对象是否继承自QPushButton


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())