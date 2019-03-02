# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSS常用控件效果")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        w=QPushButton("按钮",self)
        w.resize(100,100)
        w.move(100,100)

        x=QRadioButton("单选",self)
        x.resize(100,100)
        x.move(200,100)

        l=QLineEdit(self)
        l.resize(100,30)
        l.move(300,100)
        l.setEchoMode(QLineEdit.Password)



if __name__=='__main__':
    from Tool import QSSTool  # 这一行可以放上面

    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    QSSTool.setQssToObj("./qss/7-qss.qss", app)
    sys.exit(app.exec_())