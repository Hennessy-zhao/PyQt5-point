# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("窗口移动")
        self.move_flag=False
        self.setup_ui()

    def setup_ui(self):
        pass

    def mousePressEvent(self, evt):
        if evt.button()==Qt.LeftButton:
            self.move_flag=True
            # QMouseEvent
            # print("鼠标按下")
            #确定两个点，鼠标第一次按下的点，窗口当前所在的原始点
            self.mouse_x=evt.globalX()
            self.mouse_y=evt.globalY()
            # print(self.mouse_x,self.mouse_y)

            self.orgiin_x=self.x()
            self.orgiin_y=self.y()

    def mouseMoveEvent(self, evt):
        if self.move_flag:

            #计算的是移动的向量
            move_x=evt.globalX()-self.mouse_x
            move_y=evt.globalY()-self.mouse_y
            # print(move_x,move_y)
            dest_x=self.orgiin_x+move_x
            dest_y=self.orgiin_y+move_y
            self.move(dest_x,dest_y)

    def mouseReleaseEvent(self, QMouseEvent):
        # print("鼠标释放")
        self.move_flag=False


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.setMouseTracking(True)
    form.show()
    sys.exit(app.exec_())