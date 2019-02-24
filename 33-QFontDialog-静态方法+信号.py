# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        label=QLabel(self)
        label.move(200,100)
        label.setText("Hennessy")

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,100)

        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(30)

        def font_sel():
            # result=QFontDialog.getFont()
            result=QFontDialog.getFont(font,self,"选择一个好看的字体")
            if result[1]:
                label.setFont(result[0])
                label.adjustSize()


        btn.clicked.connect(font_sel)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())