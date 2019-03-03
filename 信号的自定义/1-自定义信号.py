# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Btn(QPushButton):
    #鼠标右击
    rightClicked=pyqtSignal([str],[int],[int,str])

    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)

        if evt.button()== Qt.RightButton:
            # print("应该发射右击信号")
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int].emit(888)
            self.rightClicked[int,str].emit(888,"xxx")
        # QMouseEvent


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号的学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn=Btn("xx",self)
        # btn.clicked.connect(lambda :print("按钮被点击了"))
        # btn.rightClicked[str].connect(lambda :print("按钮被点击了"))
        btn.rightClicked[int].connect(lambda val:print("按钮被点击了",val))
        btn.rightClicked[int,str].connect(lambda val,x:print("按钮被点击了",val,x))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())