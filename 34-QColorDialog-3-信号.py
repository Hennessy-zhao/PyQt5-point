# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):


        btn=QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")

        def test():
            cd = QColorDialog(self)

            def selColor(color):
                palette=QPalette()
                palette.setColor(QPalette.ButtonText,color)
                btn.setPalette(palette)

            # cd.colorSelected.connect(selColor)
            cd.currentColorChanged.connect(selColor)
            cd.show()

        btn.clicked.connect(test)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())