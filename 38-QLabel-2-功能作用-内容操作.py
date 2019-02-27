# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label=QLabel(self)
        label.resize(400,400)

        #数值数据
        # label.setText("<img src='images/1.png' width=60 height=60>")
        # label.setNum(888.88)

        #图形图像
        # pic=QPicture()
        # painter=QPainter(pic)
        # painter.setBrush(QBrush(QColor(100,200,100)))
        # painter.drawEllipse(0,0,200,200)
        # label.setPicture(pic)

        #动图
        # movie=QMovie('images/test.gif')
        #         # label.setMovie(movie)
        #         # label.setScaledContents(True)
        #         # movie.start()
        #         # movie.setSpeed(100)         #速度是原来的1倍

        #清空
        label.clear()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())