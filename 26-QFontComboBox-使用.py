# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontComboBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("社会我顺哥，人狠话不多")
        label.move(100,100)

        fcb=QFontComboBox(self)
        fcb.currentFontChanged.connect(lambda font:label.setFont(font))




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())