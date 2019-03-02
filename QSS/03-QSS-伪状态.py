# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        btn1=QPushButton("按钮1",self)
        btn1.move(150,50)

        cb=QCheckBox("复选框",self)
        cb.setTristate(True)
        cb.resize(100,100)
        cb.move(150,100)

        # btn1.setEnabled(False)



if __name__=='__main__':
    from Tool import QSSTool            #这一行可以放上面

    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    QSSTool.setQssToObj("./qss/3-qss.qss",app)

    sys.exit(app.exec_())