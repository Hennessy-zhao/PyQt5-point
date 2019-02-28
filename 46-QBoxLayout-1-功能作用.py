# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QBoxLayout")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:orange")

        # 1.创建布局管理器对象
        layout=QBoxLayout(QBoxLayout.LeftToRight)

        # 2.把布局管理器对象设置给需要布局的父控件
        self.setLayout(layout)

        # 3.添加需要布局的子控件到布局管理器当中
        layout.addWidget(label1)
        layout.addSpacing(100)              #添加空白
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        #添加空白
        layout.insertSpacing(4,60)

        #插入控件
        # layout.insertWidget(1,label4)

        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        h_layout = QBoxLayout(QBoxLayout.BottomToTop)
        h_layout.addWidget(label5)
        h_layout.addWidget(label6)
        h_layout.addWidget(label7)

        #插入布局
        layout.insertLayout(2,h_layout)

        #移除控件
        # layout.removeWidget(label1)         #直接移除会出现问题,需要删除或者隐藏控件
        # label1.hide()       #或者 label1.setParent(None)



        #修改方向
        # timer=QTimer(self)
        # def test():
        #     layout.setDirection((layout.direction()+1)%4)
        #
        # timer.timeout.connect(test)
        # timer.start(1000)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())