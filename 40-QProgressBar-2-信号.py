# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pb=QProgressBar(self)

        timer=QTimer(pb)

        def change_progress():
            if pb.value()==pb.maximum():
                timer.stop()

            pb.setValue(pb.value()+1)

        timer.timeout.connect(change_progress)

        timer.start(100)       #时间间隔：0.1秒

        pb.valueChanged.connect(lambda val:print("当前的进度值为：",val))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())