# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # pd=QProgressDialog(self)            #自动弹出，但是有时间间隔，默认4秒
        pd=QProgressDialog("xx1","xx2",1,1000,self)
        pd.setWindowTitle("标题")
        pd.setAutoClose(False)              #满值后不自动关闭
        pd.setAutoReset(False)              #满值后不自动重置
        # pd.open(lambda :print("对话框被取消"))
        pd.show()

        # pd.setMinimumDuration(0)            #设置等待时间为0

        for i in range(1,101):
            # import time
            # time.sleep(1)
            pd.setValue(i)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())