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
        lcd=QLCDNumber(self)
        lcd.move(0, 0)
        lcd.resize(300, 100)

        lcd.setDigitCount(2)

        #模式设置
        # lcd.setMode(QLCDNumber.Bin)     #设置为二进制
        # lcd.setMode(QLCDNumber.Oct)     #设置为八进制
        #lcd.setMode(QLCDNumber.Hex)     #设置为十六进制

        #溢出判定
        # lcd.checkOverflow(99)
        # lcd.overflow.connect(lambda :print("溢出"))

        #分段样式
        lcd2=QLCDNumber(self)
        lcd2.move(0,100)
        lcd2.resize(300,100)

        lcd3 = QLCDNumber(self)
        lcd3.move(0, 200)
        lcd3.resize(300, 100)

        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)

        lcd.display(99)
        lcd2.display(99)
        lcd3.display(99)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())