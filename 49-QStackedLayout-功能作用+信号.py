# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # 1.创建一个布局管理器对象
        sl=QStackedLayout()             #同一时间只能看到一个控件

        # 2.把布局对象设置给需要布局的父控件，父布局    很重要，先做这一步
        self.setLayout(sl)          #也可以直接写sl=QStackedLayout(self)

        # 3.通过布局对象，管理布局一些子控件
        # 创建3个子空间
        label1 = QLabel("标签1")
        label1.setStyleSheet("background-color:cyan")

        label2 = QLabel("标签2")
        label2.setStyleSheet("background-color:yellow")

        label3 = QLabel("标签3")
        label3.setStyleSheet("background-color:red")

        label4 = QLabel("标签4")
        label4.setStyleSheet("background-color:red")

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


        #添加控件
        sl.addWidget(label1)
        sl.addWidget(label2)
        sl.addWidget(label3)

        #插入控件
        # print(sl.currentIndex())            #目前展示的索引值
        # print(sl.insertWidget(1, label4))

        #切换子控件
        # sl.setCurrentIndex(1)
        # timer=QTimer(self)
        # timer.timeout.connect(lambda :sl.setCurrentIndex((sl.currentIndex()+1)%sl.count()))
        # timer.start(1000)

        # sl.currentWidget(label2)        #设置目前展示的子控件

        #展示模式控制
        sl.setStackingMode(QStackedLayout.StackAll)        #所有小部件都可见。当前控件显示在最前。
        label1.hide()           #标签2可以看到

        #信号
        # sl.currentChanged.connect(lambda val:print(val))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())