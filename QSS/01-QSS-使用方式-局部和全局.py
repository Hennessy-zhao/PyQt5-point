# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        box1=QWidget(self)
        box2=QWidget(self)

        #局部样式
        # box1.setStyleSheet("QPushButton{background-color:orange;}")
        # box2.setStyleSheet("background-color:cyan")

        label1=QLabel("标签1",box1)
        label1.setObjectName("lab1")
        label1.move(50,50)
        btn1=QPushButton("按钮1",box1)
        btn1.move(150,50)

        label2 = QLabel("标签2", box2)
        label2.move(50, 50)
        btn2 = QPushButton("按钮2", box2)
        btn2.setObjectName("b2")
        btn2.move(150, 50)

        v_layout=QVBoxLayout()
        self.setLayout(v_layout)

        v_layout.addWidget(box1)
        v_layout.addWidget(box2)

        self.other_btn=QPushButton("按钮3")
        self.other_btn.show()


if __name__=='__main__':
    from Tool import QSSTool            #这一行可以放上面

    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    QSSTool.setQssToObj("./qss/test.qss",app)

    sys.exit(app.exec_())