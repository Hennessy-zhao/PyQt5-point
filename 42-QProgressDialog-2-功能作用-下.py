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
        pd=QProgressDialog(self)
        #pd.setAutoReset(False)          #关闭自动重置

        #设置范围
        pd.setRange(0,500)
        # print(pd.minimum())
        # print(pd.maximum())

        pd.show()

        timer=QTimer(pd)

        def test():
            # print(pd.value())
            if pd.value()+1>=pd.maximum() or pd.wasCanceled():
                timer.stop()
                # print(pd.autoClose())

            pd.setValue(pd.value() + 1)

        timer.timeout.connect(test)
        timer.start(10)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())