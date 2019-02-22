# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # dt=QDateTime(2018,12,12,12,30)
        # dt=QDateTime.currentDateTime()
        # # dt1=dt.addYears(2)       #返回一个新的值，但是并没有显示出来
        # dt1=dt.addYears(-2)
        # print(dt.offsetFromUtc()//3600)     #算相差多少小时
        # # print(dt1)
        # QDateTimeEdit(dt1,self)
        # QDate
        # QTime
        time=QTime.currentTime()
        time.start()

        btn=QPushButton(self)
        btn.setText("测试")
        btn.move(200,200)
        btn.clicked.connect(lambda :print(time.elapsed()))          #经历的毫秒数



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())