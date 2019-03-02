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
        label = QLabel("标签测试", self)
        label.resize(300, 300)
        label.move(100, 100)

        self.qss边框(label)

    def qss边框(self, label):
        label.setStyleSheet("""
            QLabel {
                background-color:rgb(100,200,100);
                background-image:url(../images/1.png);
                background-repeat:no-repeat;
                background-position:right bottom;
                background-origin:margin;
                background-clip:padding
            }
        """)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Demo()
    form.show()

    sys.exit(app.exec_())