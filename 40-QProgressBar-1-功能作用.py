# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPregressBar")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pb=QProgressBar(self)

        pb.resize(400,40)

        # print(pb.minimum())         # 最小值是 0
        # print(pb.maximum())         # 最大值是 100

        # pb.setMinimum(50)
        pb.setRange(0,100)
        pb.setValue(75)

        # pb.reset()

        btn=QPushButton(self)
        btn.move(200,200)
        btn.setText("测试按钮")

        def test():
            # pb.reset()
            # print(pb.minimum())
            # print(pb.maximum())
            # print(pb.value())
            # pb.resetFormat()
            # pb.setAlignment(Qt.AlignHCenter)

            # print(pb.text())        #获取文本
            pb.setOrientation(Qt.Vertical)      #刻度条变成纵向
            pb.resize(40,400)

            pb.setInvertedAppearance(True)      #倒立外观

        btn.clicked.connect(test)

        pb.setFormat("当前人数 {} /总人数 %m".format(pb.value()-pb.minimum()))

        # pb.setTextVisible(False)        #文本不可见

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())