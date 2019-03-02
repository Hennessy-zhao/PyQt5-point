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
        label.move(100,100)

        label.setStyleSheet("""
            QLabel {
                font-family:微软雅黑;
                font-size:20px;
                font-style:italic;
                font-weight:900;
                color:orange;
                
                min-width:200px;
                min-height:200px;
                
                max-width:600px;
                max-height:600px;
            }
        """)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())