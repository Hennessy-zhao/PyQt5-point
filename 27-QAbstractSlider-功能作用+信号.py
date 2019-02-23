# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # QAbstractSlider
        label=QLabel(self)
        label.setText("0")
        label.move(200,200)
        label.resize(100,30)

        sd=QSlider(self)
        sd.move(100,100)

        # #设置最大值最小值
        # sd.setMaximum(100)
        # sd.setMinimum(50)
        #
        # #当前数值
        # sd.setValue(88)
        #
        # #步长设置
        # # sd.setSingleStep(5)
        # sd.setPageStep(8)
        #
        # #跟踪设置
        # print(sd.hasTracking())
        # sd.setTracking(False)       #拖拽过程中数值不改变

        #滑块位置设置
        # sd.setSliderPosition(88)

        #倒立外观
        # sd.setInvertedAppearance(True)

        #操作反转
        # sd.setInvertedControls(True)

        #滑块方向
        # sd.setOrientation(Qt.Horizontal)


        #信号
        # sd.valueChanged.connect(lambda val:label.setText(str(val)))
        sd.valueChanged.connect(lambda: label.setText(str(sd.value())))

        # sd.sliderMoved.connect(lambda val:print(val))

        # sd.actionTriggered.connect(lambda val:print(val))

        sd.rangeChanged.connect(lambda min,max:print(min,max))      #当范围发生改变时

        sd.setMaximum(200)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())