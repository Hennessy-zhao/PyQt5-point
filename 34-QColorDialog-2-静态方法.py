# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cd = QColorDialog(QColor(100, 200, 150), self)
        # 标准颜色
        QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        QColorDialog.setCustomColor(0, QColor(100, 200, 0))        #自定义颜色框
        # QColorDialog.setCustomColor(3, QColor(100, 200, 200))

        cd.show()


        btn=QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")

        def test():
            color=QColorDialog.getColor(QColor(10,20,100),self,"选择颜色")
            print(color)
        btn.clicked.connect(test)

        # btn.clicked.connect(lambda :print(QColorDialog.customCount()))            #自定义颜色个数，静态函数，也可以写成 cd.customCount()
        # btn.clicked.connect(lambda :print())


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())