# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # mb=QMessageBox(self)
        mb=QMessageBox(QMessageBox.Warning,"xx1","<h2>xx2</2>",QMessageBox.Ok | QMessageBox.Discard,self)
        # mb.setModal(False)          #非模态
        # mb.setWindowModality(Qt.NonModal)       #非模态

        # mb.show()
        # mb.exec_()
        mb.open()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())