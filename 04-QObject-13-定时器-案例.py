# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class MyLabel(QLabel):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.move(100,100)
        self.setStyleSheet("font-size:30px")
        self.setText("10")
        self.setText("10")


    def setSec(self,sec):
        self.setText(str(sec))

    def startMyTimer(self,ms):
        self.timer_id=self.startTimer(ms)


    def timerEvent(self, *args, **kwargs):
        #print("xx")
        #获取当前标签的内容
        current_sec=int(self.text())
        current_sec-=1
        self.setText(str(current_sec))

        if current_sec==0:
            #停掉定时器
            self.killTimer(self.timer_id)        #放入那个定时器的id

class MyWidget(QWidget):

    def timerEvent(self, *args, **kwargs):
        current_w=self.width()
        current_h=self.width()
        self.resize(current_w+10,current_h+10)


app=QApplication(sys.argv)


window=MyWidget()

#例子：1创建一个定时器
label=MyLabel(window)
label.setSec(5)
label.startMyTimer(1000)

#例子2：窗口不断变大
window.startTimer(100)


window.show()

sys.exit(app.exec_())