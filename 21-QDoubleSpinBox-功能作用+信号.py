# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        return str(p_float)+"*"+str(p_float)

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # dsb=QDoubleSpinBox(self)
        dsb=MyDoubleSB(self)
        dsb.move(100,100)
        dsb.resize(100,30)

        # dsb.setMaximum(88.88)
        # dsb.setMinimum(22.22)
        # dsb.setSingleStep(0.02)
        # dsb.setWrapping(True)
        #
        # dsb.setPrefix("$")
        # dsb.setSuffix("%")

        #最小值特殊文本
        # dsb.setRange(1.0,2.0)
        # dsb.setSingleStep(0.5)
        # dsb.setSuffix("倍速")
        # dsb.setWrapping(True)
        # dsb.setSpecialValueText("正常")

        #设置位数
        # dsb.setDecimals(1)

        test_button=QPushButton(self)
        test_button.move(300,300)
        test_button.setText("测试按钮")
        # test_button.clicked.connect(lambda :dsb.setValue(66.666))
        # test_button.clicked.connect(lambda :print(dsb.value()))
        test_button.clicked.connect(lambda :print(dsb.cleanText()))

        # dsb.valueChanged.connect(lambda val:print(val))
        dsb.valueChanged[str].connect(lambda val:print(val))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())