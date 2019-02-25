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
        # self.setStyleSheet("background-color:rgb(100,200,150)")

        cd=QColorDialog(QColor(100,200,150),self)
        cd.setWindowTitle("选择一个好看的颜色")

        #选项控制
        cd.setOption(QColorDialog.NoButtons)  # 不显示ok和cancel按钮
        cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)


        def color(col):
            pattle = QPalette()
            pattle.setColor(QPalette.Background,col )
            self.setPalette(pattle)
        cd.colorSelected.connect(color)

        def colors():
            pattle = QPalette()
            pattle.setColor(QPalette.Background, cd.selectedColor())
            self.setPalette(pattle)
        cd.show()
        # cd.open(colors)
        # if cd.exec_():
        #     colors()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())