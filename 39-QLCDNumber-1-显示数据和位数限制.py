# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLCDNumber")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # lcd=QLCDNumber(self)
        lcd=QLCDNumber(5,self)      #5表示位数，展示5位
        lcd.move(100,100)
        lcd.resize(300,50)

        # lcd.setDigitCount(8)        #设置位数

        # 0 / O, 1, 2, 3, 4, 5 / S, 6, 7, 8, 9 / g
        # A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y
        # : ' 空格

        # lcd.display("osgabcdefhLPruU")
        # lcd.display(": ' ")
        # lcd.display(888666)     #显示0，溢出
        lcd.display(88854.666)
        # lcd.display(-88854.666)   #产生溢出，可以表示负数

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(50,50)
        btn.clicked.connect(lambda :print(lcd.value()))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())