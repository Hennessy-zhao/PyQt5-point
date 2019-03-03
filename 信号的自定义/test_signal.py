# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Btn(QPushButton):
    #鼠标右击
    rightClicked=pyqtSignal([str],[int])

    def mousePressEvent(self,evt):
        super().mousePressEvent(evt)

        if evt.button()== Qt.RightButton:
            # print("应该发射右击信号")
            self.rightClicked[str].emit(self.text())
            self.rightClicked[int].emit(888)
        # QMouseEvent