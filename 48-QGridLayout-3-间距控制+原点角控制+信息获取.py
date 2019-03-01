# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        gl=QGridLayout()

        self.setLayout(gl)

        # 创建3个子空间
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        # 布局的嵌套
        label5 = QLabel("标签5")
        label5.setStyleSheet("background-color:pink")

        label6 = QLabel("标签6")
        label6.setStyleSheet("background-color:blue")

        label7 = QLabel("标签7")
        label7.setStyleSheet("background-color:cyan")

        v_layout = QVBoxLayout()
        v_layout.addWidget(label5)
        v_layout.addWidget(label6)
        v_layout.addWidget(label7)

        gl.addWidget(label1,0,0)
        gl.addWidget(label2,0,1)
        gl.addWidget(label3,1,0,3,3)            #占3行，占3列

        gl.addLayout(v_layout,4,0,1,4)

        #间距控制
        # print(gl.spacing())
        # print(gl.horizontalSpacing())
        # print(gl.verticalSpacing())
        gl.setVerticalSpacing(60)           #设置行与行之间间距
        gl.setHorizontalSpacing(30)         #设置列与列之间间距

        #原点角设置
        # gl.setOriginCorner(Qt.TopRightCorner)       #右上角为原点角（从右往左，从上往下）
        # gl.setOriginCorner(Qt.BottomLeftCorner)       #左下角为原点角（从左往右，从下往上）


        #信息获取
        print(gl.rowCount())
        print(gl.columnCount())

        # print(gl.cellRect(0, 1))  # 获取区域为空


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    gl=form.layout()
    print(gl.cellRect(0, 1))  # 获取区域(138, 11, 97, 48)       父控件显示完全之后才能获取内部子空间的尺寸

    sys.exit(app.exec_())