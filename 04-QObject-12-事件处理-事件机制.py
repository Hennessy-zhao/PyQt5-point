# -*- coding:UTF-8 -*-
from PyQt5.Qt import *
import sys


class App(QApplication):
    #重写
    def notify(self, reciver, evt):
        if reciver.inherits("QPushButton") and evt.type()==QEvent.MouseButtonPress:
            print(reciver,evt)

        return super().notify(reciver,evt)

class Btn(QPushButton):
    #重写
    def event(self, evt):
        if evt.type()==QEvent.MouseButtonPress:
            print(evt)
        return super().event(evt)

    def mousePressEvent(self, *args, **kwargs):
        print("鼠标被按下了.....")
        return super().mousePressEvent(*args,**kwargs)

app=App(sys.argv)

window=QWidget()

btn=Btn(window)
btn.setText("按钮")
btn.move(100,100)

def cao():
    print("按钮被点击了")

btn.pressed.connect(cao)

window.show()

sys.exit(app.exec_())