# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        gl = QGridLayout()

        self.setLayout(gl)

        # 创建3个子空间
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        gl.addWidget(label1, 0, 0)
        gl.addWidget(label2, 0, 1)
        gl.addWidget(label3, 1, 0, 3, 3)

        # gl.setColumnMinimumWidth(0,100)            #设置第0列的最小宽度
        # gl.setRowMinimumHeight(0,100)              #设置第0行的最小宽度

        gl.setColumnStretch(0,2)     #调整第0列的拉伸系数为2
        gl.setColumnStretch(1,1)     #调整第1列的拉伸系数为1

        gl.setRowStretch(0,1)           #调整第0行的拉伸系数


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())