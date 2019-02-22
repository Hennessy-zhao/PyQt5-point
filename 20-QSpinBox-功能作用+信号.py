# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#自定义展示格式
class SB(QSpinBox):
    def textFromValue(self, p_int):
        print(p_int)
        #1*1
        return  str(p_int)+"*"+str(p_int)

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        asb=SB(self)
        asb.resize(100,25)
        asb.move(100,100)


        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150,150)

        #设置数值循环
        # btn.clicked.connect(lambda :self.数值循环())

        #设置步长
        # btn.clicked.connect(lambda :self.步长设置())

        #设置前缀和后缀
        # btn.clicked.connect(lambda :self.前缀和后缀())

        #设置进制
        # btn.clicked.connect(lambda :self.设置进制())

        #设置以及获取数值
        btn.clicked.connect(lambda :self.设置以及获取数值())

        self.asb=asb

        # #设置范围
        # self.最大值最小值()
        # self.asb.valueChanged.connect(lambda val: print(type(val), val))
        self.asb.valueChanged[str].connect(lambda val:print(type(val),val))

    def 最大值最小值(self):
        #设置最大值
        # self.asb.setMaximum(180)
        # print(self.asb.maximum())

        #设置最小值
        # self.asb.setMinimum(18)
        # print(self.asb.minimum())

        #设置范围
        self.asb.setRange(18,180)

    def 数值循环(self):
        self.asb.setWrapping(True)

    def 步长设置(self):
        self.asb.setSingleStep(3)

    def 前缀和后缀(self):
        # self.asb.setRange(1,12)
        # self.asb.setSuffix("月")         #添加后缀

        self.asb.setRange(0,6)
        self.asb.setPrefix("周")
        self.asb.setSpecialValueText("周日")      #设置最小值特殊文本

    def 设置进制(self):
        self.asb.setDisplayIntegerBase(2)

    def 设置以及获取数值(self):
        self.asb.setValue(66)
        # print(self.asb.value())



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())