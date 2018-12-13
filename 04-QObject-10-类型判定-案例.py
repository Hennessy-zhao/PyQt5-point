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
        label1=QLabel(self)
        label1.setText("社会我顺哥")
        label1.move(100,100)

        label2=QLabel(self)
        label2.move(200,200)
        label2.setText("人狠话不多")

        btn=QPushButton(self)
        btn.move(300,300)
        btn.setText("点我")

        for widget in self.children():
            #print(widget)
            if widget.inherits("QLabel"):           #判断对象是否继承自QLabel类
                widget.setStyleSheet("color:green")
                print("是")



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())