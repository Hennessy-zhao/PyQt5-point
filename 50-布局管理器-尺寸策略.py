# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Label(QLabel):

    #建议的最小尺寸大小
    def minimumSizeHint(self):
        return QSize(200,200)

    #建议的尺寸大小
    def sizeHint(self):
        return QSize(150,60)

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label1 = Label("标签1")
        # label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")


        layout=QVBoxLayout()
        self.setLayout(layout)

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        #尺寸策略
        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)       #水平和垂直方向的尺寸策略，都不能伸展
        sp=QSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
        sp.setRetainSizeWhenHidden(True)                    # 如果隐藏，则保留尺寸，必须放在setSizePolicy之前
        label1.setSizePolicy(sp)

        label1.setFixedSize(300,300)        #优先级最高

        label1.hide()

        # label1.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Ignored)
        # label2.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Expanding)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())