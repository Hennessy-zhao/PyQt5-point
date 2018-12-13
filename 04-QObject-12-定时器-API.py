# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class MyObject(QObject):
    def timerEvent(self, evt):
        print(evt,"1")

app=QApplication(sys.argv)


obj=MyObject()
timer_id=obj.startTimer(1000)

obj.killTimer(timer_id)     #删除计数器


sys.exit(app.exec_())