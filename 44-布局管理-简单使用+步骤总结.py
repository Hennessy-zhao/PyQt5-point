# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("布局管理")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 创建3个子空间
        label=QLabel("标签1")
        label.setStyleSheet("background-color:cyan")

        labe2 = QLabel("标签2")
        labe2.setStyleSheet("background-color:yellow")

        labe3 = QLabel("标签3")
        labe3.setStyleSheet("background-color:red")

        #布局管理器实现方式
        v_layout=QVBoxLayout()      #竖直排列
        v_layout.addWidget(label)
        v_layout.addWidget(labe2)
        v_layout.addWidget(labe3)

        v_layout.setContentsMargins(20,30,40,50)            #左、上、右、下
        v_layout.setSpacing(60)

        self.setLayout(v_layout)

        # 布局方向
        self.setLayoutDirection(Qt.RightToLeft)

        print(self.children())

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())