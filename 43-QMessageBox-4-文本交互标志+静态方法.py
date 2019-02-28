# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        #静态方法

        # QMessageBox.about(self,"xx1","xx2")
        # QMessageBox.aboutQt(self,"xx1")
        result=QMessageBox.question(self,"xx1","xx2",QMessageBox.Ok | QMessageBox.No,QMessageBox.No)
        print(result,"xxx")

        #下面的先注释掉
        return None
        mb=QMessageBox(self)

        mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)             #设置标准按钮

        #文本交互标志
        mb.setTextInteractionFlags(Qt.TextEditorInteraction)                #可以和文本进行交互，仅控制主标题



        mb.open()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())