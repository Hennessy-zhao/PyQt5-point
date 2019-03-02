# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QSpinBox(self)
        label.resize(300,300)
        label.move(100, 100)

        label.setStyleSheet("""
            QSpinBox{
                font-size:26px;
                color:orange;
                border:10px double red;
                border-radius:10px;
                background-color:lightgrey;
                
            }
            
            QSpinBox::up-button,QSpinBox::down-button{
                width:50px;
                height:50px;
            }
            
            QSpinBox::up-button{
                subcontrol-origin:padding;
                subcontrol-position:left center;
                image:url(../images/up.png);
            }
            
            QSpinBox::up-button:hover{
                bottom:10px;
            }
            
            QSpinBox::down-button{
                subcontrol-origin:padding;
                subcontrol-position:right center;
                image:url(../images/down.png);
            }
            
            QSpinBox::down-button:hover{
                position: absolute;
                top:10px;
            }
            
        """)

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Demo()
    form.show()
    sys.exit(app.exec_())