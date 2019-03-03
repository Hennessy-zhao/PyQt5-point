# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test_zhuangshiqi_signal_slot import Ui_Form
import sys

class Demo(QWidget,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500,500)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print("按钮被点击了")

    @pyqtSlot()
    def on_pushButton_pressed(self):
        print("按钮被按下")


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())