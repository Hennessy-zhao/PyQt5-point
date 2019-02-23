# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class Slider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.setTickPosition(QSlider.TicksBothSides)
        self.setup_ui()

    def setup_ui(self):
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.setStyleSheet("color:red")
        self.label.hide()

    def mousePressEvent(self, evt):
        # QMouseEvent
        super().mousePressEvent(evt)
        x=(self.width()-self.label.width())/2
        y=(1-self.value()/(self.maximum()-self.minimum()))*self.height()-self.label.height()
        self.label.show()
        self.label.move(x,y)
        # print(x,y)

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        x = (self.width() - self.label.width()) / 2
        y = (1 - self.value() / (self.maximum() - self.minimum())) * (self.height()-self.label.height())
        self.label.move(x, y)
        # print(x, y)
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseReleaseEvent(self, evt):
        super().mouseReleaseEvent(evt)
        self.label.hide()

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider拓展案例")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 0.创建两个控件
        slider=Slider(self)
        slider.move(200,200)
        slider.resize(30,200)






if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())