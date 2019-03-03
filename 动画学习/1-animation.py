# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("动画学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        btn=QPushButton("测试按钮",self)
        btn.move(100,100)
        btn.resize(200,200)
        btn.setStyleSheet("background-color:cyan;")

        # 1 创建一个动画对象，并且设置目标  属性
        # animation=QPropertyAnimation(self)
        # animation.setTargetObject(btn)
        # animation.setPropertyName(b"pos")               #设置属性为位置

        animation = QPropertyAnimation(btn,b"pos",self)         #设置属性为位置
        # animation = QPropertyAnimation(btn,b"size",self)            #设置属性为大小
        # animation = QPropertyAnimation(btn,b"geometry",self)            #设置属性为geomotry(size和pos同时)
        # animation = QPropertyAnimation(self,b"windowOpacity",self)            #设置窗口透明度变化的动画

        # 2 设置属性值 开始 差值 结束
        animation.setStartValue(QPoint(0,0))                #属性为位置时设置起始和结束
        animation.setEndValue(QPoint(300,300))

        # animation.setStartValue(QSize(0, 0))               #属性为大小时设置起始和结束
        # animation.setEndValue(QSize(300, 300))

        # animation.setStartValue(QRect(0, 0,100,100))                # 属性为geomitry时设置起始和结束
        # animation.setEndValue(QRect(200, 200,300,300))

        # animation.setStartValue(1)                                  # 属性为windowOpacity时设置起始和结束
        # animation.setKeyValueAt(0.5,0)                                   #第一个值为在某个位置插入一个值，值为0-1
        # animation.setEndValue(1)

        # 3 动画时长
        animation.setDuration(3000)         #3000毫秒

        #循环个数（基类QAbstractAnimation的方法）
        animation.setLoopCount(3)

        #设置动画曲线  https://doc.qt.io/qt-5/qeasingcurve.html#Type-enum
        # animation.setEasingCurve(QEasingCurve.InQuad)
        # animation.setEasingCurve(QEasingCurve.OutQuad)
        # animation.setEasingCurve(QEasingCurve.InBounce)                 #弹簧效果
        animation.setEasingCurve(QEasingCurve.OutBounce)                 #弹簧效果

        #方向设置
        # animation.setDirection(QAbstractAnimation.Backward)              #倒着走

        # 4 启动动画
        animation.start()


        # btn.clicked.connect(lambda :print(animation.loopCount(),animation.currentLoop()))           #动画循环总个数和目前是第几次循环
        # btn.clicked.connect(lambda :print(animation.totalDuration(),animation.duration()))              #动画总时长，动画单次时长
        # btn.clicked.connect(lambda :print(animation.currentTime(),animation.currentLoopTime()))              #当前时长，当前循环内的时间

        #点击一次，暂停；再点击，继续
        self.flag=True
        def animation_operation():
            # if self.flag:
            #     animation.pause()
            #     self.flag=False
            # else:
            #     animation.resume()
            #     self.flag=True

            #或者不用flag，直接判断动画状态
            if animation.state()==QAbstractAnimation.Running:
                animation.pause()                               #如果改成stop,则状态变成QAbstractAnimation.Stopped
            elif animation.state()==QAbstractAnimation.Paused:
                animation.resume()
            elif animation.state()==QAbstractAnimation.Stopped:             #动画stop之后无法恢复resume
                animation.resume()

        btn.clicked.connect(animation_operation)


        #信号
        animation.currentLoopChanged.connect(lambda val:print("当前循环次数发生改变",val))
        animation.finished.connect(lambda :print("动画执行完毕"))
        animation.stateChanged.connect(lambda ns,os:print("状态发生改变",ns,os))              #pause状态是1，running状态是2,stop是0




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())