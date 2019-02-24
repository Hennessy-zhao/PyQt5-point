# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("案例")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 0.添加子空间，复选框

        for i in range(0,30):
            cb=QCheckBox(self)
            cb.setText("{}".format(i))
            cb.move(i%4*50,i//4*60)

        # 1.创建一个橡皮筋选中控件
        self.rb = QRubberBand(QRubberBand.Rectangle, self)

    def mousePressEvent(self, evt):
        QMouseEvent

        #2,尺寸大小；鼠标点击的位置点，00
        self.origin_pos=evt.pos()
        self.rb.setGeometry(QRect(self.origin_pos,QSize()))

        #3.展示橡皮筋控件
        self.rb.show()

    def mouseMoveEvent(self, evt):
        #调整橡皮筋选中控件的位置以及尺寸
        self.rb.setGeometry(QRect(self.origin_pos,evt.pos()).normalized())      #normalized是为了实现这个矩形从右下角往左上角拖拽出现了两个点有负
        pass

    def mouseReleaseEvent(self, evt):
        #1.获取橡皮筋控件尺寸的范围
        rect=self.rb.geometry()
        #2.遍历所有的子控件，查看，那些子控件在尺寸范围
        for child in self.children():
            if rect.contains(child.geometry()) and child.inherits("QCheckBox"):
                child.toggle()

        self.rb.hide()



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())