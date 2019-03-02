# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS级联和冲突")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn1=QPushButton("b1",self)
        btn2=QPushButton("b2",self)
        btn1.setObjectName("b1")
        btn2.setObjectName("b2")

        btn1.move(100,100)
        btn2.move(200,200)

        self.setStyleSheet("""
            QPushButton{
                color:red;
            }
            
            QPushButton#b1{
                color:orange;
            }
            
            QPushButton:hover{
                color:green;
            }
            
        """)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())