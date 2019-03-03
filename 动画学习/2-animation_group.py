# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动画组")
        self.resize(800,800)
        self.setup_ui()

    def setup_ui(self):

        #红色逆时针，绿色顺时针
        red_btn=QPushButton("红色按钮",self)
        green_btn=QPushButton("绿色按钮",self)

        red_btn.resize(100,100)
        green_btn.resize(100,100)
        green_btn.move(150,150)

        red_btn.setStyleSheet("""
            background-color:red;
        """)

        green_btn.setStyleSheet("""
            background-color:green;
        """)


        #动画设置
        #绿色
        animation=QPropertyAnimation(green_btn,b"pos",self)

        animation.setKeyValueAt(0,QPoint(150,150))
        animation.setKeyValueAt(0.25,QPoint(550,150))
        animation.setKeyValueAt(0.5,QPoint(550,550))
        animation.setKeyValueAt(0.75,QPoint(150,550))
        animation.setKeyValueAt(1,QPoint(150,150))

        animation.setDuration(1000)
        animation.setLoopCount(3)

        # animation.start()


        #红色
        animation2 = QPropertyAnimation(red_btn, b"pos", self)

        animation2.setKeyValueAt(0, QPoint(0, 0))
        animation2.setKeyValueAt(0.25, QPoint(0, 700))
        animation2.setKeyValueAt(0.5, QPoint(700, 700))
        animation2.setKeyValueAt(0.75, QPoint(700, 0))
        animation2.setKeyValueAt(1, QPoint(0, 0))

        animation2.setDuration(1000)
        animation2.setLoopCount(3)

        # animation2.start()


        #并行动画
        # animation_group1=QParallelAnimationGroup(self)
        # animation_group1.addAnimation(animation)  # 添加动画
        # animation_group1.addAnimation(animation2)
        # animation_group1.start()

        # 串行动画
        animation_group1=QSequentialAnimationGroup(self)
        animation_group1.addAnimation(animation)             #添加动画
        # animation_group1.addPause(5000)         #暂停动画

        #暂停动画，和上面一行作用一致
        pause_animation=QPauseAnimation()
        pause_animation.setDuration(3000)
        animation_group1.addAnimation(pause_animation)

        animation_group1.addAnimation(animation2)
        animation_group1.start()

        #按红色暂停，绿色开始
        red_btn.clicked.connect(animation_group1.pause)
        green_btn.clicked.connect(animation_group1.resume)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())