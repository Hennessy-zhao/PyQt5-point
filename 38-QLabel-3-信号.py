# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label=QLabel("Hennessy在学习哈哈哈 <a href='www.baidu.com'>百度</a>",self)

        # label.linkHovered.connect(lambda a:print(a))            #鼠标放上去，传递一个参数是网址
        label.linkActivated.connect(lambda a:print(a))              #鼠标点击，传递一个参数是网址

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())