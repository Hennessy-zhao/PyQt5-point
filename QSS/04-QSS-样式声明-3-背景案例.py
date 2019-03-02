# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("背景案例")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QPushButton{
                background-image:url(../images/puke.png);
                border:20px double red;
                background-origin:content;
                background-clip:padding;
            }
        """)
        h_layout=QHBoxLayout(self)
        for i in range(0,13):

            btn=QPushButton(self)
            btn.resize(90,106)
            btn.setFixedSize(90,106)

            btn.setStyleSheet("""
                    QPushButton{
                        padding-left:-%dpx;
                        padding-top:-%dpx;
                        
                    }
            """%(i*49,0))

            h_layout.addWidget(btn)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())