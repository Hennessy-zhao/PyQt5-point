# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        rb=QRubberBand(QRubberBand.Rectangle,self)
        rb.setGeometry(10,10,60,80)
        rb.setVisible(True)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())