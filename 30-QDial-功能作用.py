# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        label=QLabel(self)
        label.move(200,100)
        label.setText("Hennessy哈哈哈")



        dia=QDial(self)

        dia.setRange(66,88)
        def test(val):
            label.setStyleSheet("font-size:{}px;".format(val))
            label.adjustSize()

        dia.valueChanged.connect(test)

        dia.setNotchesVisible(True)         #显示刻度
        dia.setPageStep(5)

        dia.setWrapping(True)           #是否包裹

        dia.setNotchTarget(10)            #凹口之间的目标像素数,控制刻度密度



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())