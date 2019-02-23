# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        sd=QSlider(self)
        sd.move(200,200)
        sd.resize(30,200)
        sd.setTickPosition(QSlider.TicksLeft)           #刻度线，目前是出现在左侧
        # sd.setPageStep(5)
        sd.setTickInterval(5)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())