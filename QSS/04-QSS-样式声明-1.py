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

        label=QLabel("标签测试",self)
        label.resize(300,300)
        label.move(0,0)

        self.qss边框(label)

    def qss边框(self,label):
        label.setStyleSheet("""
            QLabel {
                background-color:qlineargradient(x1:0, y1:0, x2:1, y2:1,stop:0 red, stop: 0.4 gray, stop:1 green);
                border-width:6px 10px 15px 20px;
                border-style:dotted dashed solid double;
                border-top-style:groove;
                border-bottom-width:30px;
                border-color:red green orange blue;
                border-left-color:#00ff00;
                border-radius:50px;
                
                border-image:url(../images/1.png) 30px 30px 30px 30px round;
                border-width:30px;
                
                margin:10px 20px 30px 40px;
                
                padding:1em;
            }
        """)


if __name__=='__main__':


    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    sys.exit(app.exec_())