# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("装饰器连接信号与槽")
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton("测试按钮",self)
        btn.setObjectName("btn")
        btn.resize(200,200)
        btn.move(100,100)

        btn2 = QPushButton("测试按钮2", self)
        btn2.setObjectName("btn2")
        btn2.resize(200, 200)
        btn2.move(100, 300)

        #装饰器自动连接信号与槽
        QMetaObject.connectSlotsByName(self)
        # btn.clicked.connect(self.click)

    @pyqtSlot(bool)                     #系统能发送的，只是一个bool值       格式为 on_objectName_信号
    def on_btn_clicked(self,val):
        print("按钮被点击了",val)

    @pyqtSlot()
    def on_btn2_clicked(self):
        print("按钮2被点击了")


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())