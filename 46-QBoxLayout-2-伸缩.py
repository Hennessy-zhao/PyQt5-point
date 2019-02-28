# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayout伸缩")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # QBoxLayout的子类
        # layout = QHBoxLayout()
        #
        # layout1 = QVBoxLayout()

        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        # 1.创建布局管理器对象
        layout = QBoxLayout(QBoxLayout.LeftToRight)

        # 2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        # 3.添加需要布局的子控件到布局管理器当中
        layout.addWidget(label1,1)
        layout.addStretch(2)                #如果不写数字，相当于在两个label中间加了一个伸缩因子
        layout.addWidget(label2,1)
        layout.addStretch(1)
        layout.addWidget(label3,1)

        #设置伸缩因子
        layout.setStretchFactor(label2,2)           #也可以给布局 layout 添加伸缩因子



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())