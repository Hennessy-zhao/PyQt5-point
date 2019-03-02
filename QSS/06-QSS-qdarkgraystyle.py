# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("三方包样式表")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        layout=QVBoxLayout(self)

        label=QLabel("xxx")
        btn=QPushButton("xx2")
        cb=QComboBox()
        cb.addItems(["1","2","3"])
        sb=QSpinBox()

        layout.addWidget(label)
        layout.addWidget(btn)
        layout.addWidget(cb)
        layout.addWidget(sb)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    import qdarkgraystyle

    sheet = qdarkgraystyle.load_stylesheet()        #也可以用load_stylesheet_pyqt5
    print(sheet)
    app.setStyleSheet(sheet)
    sys.exit(app.exec_())