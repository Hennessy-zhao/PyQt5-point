# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")

        self.setup_ui()


    def setup_ui(self):
        '''案例1'''
        # btn=QPushButton(self)
        # btn.setText("点击我")
        #
        # def cao():
        #     print("点我干啥")
        #
        # btn.clicked.connect(cao)
        pass


if __name__=='__main__':
    app=QApplication(sys.argv)


    '''案例2'''
    window=QWidget()

    #连接窗口标题变化的信号 与 槽
    def cao(title):
        print("窗口标题变化了",title)
        window.windowTitleChanged.disconnect()
        #或者用下面一行
        #window.blockSignals(True)
        window.setWindowTitle(title+"--By Hennessy")
        window.windowTitleChanged.connect(cao)
        # 或者用下面一行,blockSignals为一个组，和上面要一致
        # window.blockSignals(False)

    window.windowTitleChanged.connect(cao)

    window.setWindowTitle("Hello Sz")

    window.setWindowTitle("Hello World")

    window.show()


    sys.exit(app.exec_())