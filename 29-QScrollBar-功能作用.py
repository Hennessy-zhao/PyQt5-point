# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QScrollBar")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        sb=QScrollBar(self)
        sb.resize(30,200)
        sb.move(100,100)

        sb2 = QScrollBar(Qt.Horizontal,self)
        sb2.resize(200, 30)
        sb2.move(150, 100)

        sb.valueChanged.connect(lambda val:print(val))
        sb.setPageStep(50)

        sb.grabKeyboard()           #捕获键盘

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())