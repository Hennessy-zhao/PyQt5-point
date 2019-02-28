# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理器详细使用")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 创建3个子空间
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        # 1 创建一个布局管理器对象
        layout=QBoxLayout(QBoxLayout.TopToBottom)

        # 2直接把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        layout.setSpacing(60)

        # print(layout.contentsMargins().left())
        # print(layout.contentsMargins().top())

        layout.setContentsMargins(20,30,40,50)

        #控件替换
        # layout.replaceWidget(label2,label4)         #需要把2隐藏，都则会出错
        # label2.setParent(None)                      #label2被释放
        # label2.destroyed.connect(lambda :print("label2被释放"))        #label2并没有被释放
        # label2.hide()


        #布局的嵌套
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        h_layout=QBoxLayout(QBoxLayout.LeftToRight)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        # 3把需要布局的子控件添加到布局管理器当中
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addLayout(h_layout)
        layout.addWidget(label3)

        # layout.setEnabled(False)                #布局能用性设置为False

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())