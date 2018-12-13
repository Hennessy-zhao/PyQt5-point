# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("事件消息学习")

        self.setup_ui()

    def setup_ui(self):
        pass

    #控件显示事件
    def showEvent(self, QShowEvent):
        print("窗口被展示了出来")

    #控件关闭事件
    def closeEvent(self, QCloseEvent):
        print("窗口被关闭了")

    #控件移动事件
    def moveEvent(self, QMoveEvent):
        print("窗口被移动了")

    #控件改变尺寸大小事件
    def resizeEvent(self, QResizeEvent):
        print("尺寸大小发生了变化")

    #鼠标进入时事件
    def enterEvent(self, QEvent):
        print("鼠标进来了")
        self.setStyleSheet("background-color:green")

    #鼠标离开时事件
    def leaveEvent(self, QEvent):
        print("鼠标离开了")
        self.setStyleSheet("background-color:white")


    #鼠标按下事件
    def mousePressEvent(self, QMouseEvent):
        print("鼠标被按下")

    #鼠标释放事件
    def mouseReleaseEvent(self, QMouseEvent):
        print("鼠标被释放")

    #鼠标双击事件
    def mouseDoubleClickEvent(self, QMouseEvent):
        print("鼠标被双击")

    #鼠标移动事件
    def mouseMoveEvent(self, QMouseEvent):
        print("鼠标移动了")      #但是如果不设置鼠标跟踪，则需要鼠标单击不放下再移动才会显示鼠标移动了

    #键盘按键按下事件
    def keyPressEvent(self, QKeyEvent):
        print("键盘上某个按键被按下了")

    #键盘按键释放事件
    def keyReleaseEvent(self, QKeyEvent):
        print("键盘上某个按键被释放了")

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MyWindow()
    form.show()
    sys.exit(app.exec_())