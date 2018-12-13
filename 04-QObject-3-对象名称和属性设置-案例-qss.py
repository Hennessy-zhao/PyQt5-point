# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QObject案例")
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_QObject(self):

        with open("QObject.qss","r") as f:
            qApp.setStyleSheet(f.read())

        label1=QLabel(self)
        label1.setObjectName("notice")
        label1.setText("Hello Word")

        label2 = QLabel(self)
        label2.setObjectName("notice")
        label2.setProperty("notice_level","normal")
        label2.move(100,100)
        label2.setText("By Hennessy")

        label3 = QLabel(self)
        label3.setObjectName("notice")
        label3.setProperty("notice_level", "warning")
        label3.move(200, 200)
        label3.setText("By Hennessy")

        label4 = QLabel(self)
        label4.setObjectName("notice")
        label4.setProperty("notice_level", "error")
        label4.move(300, 300)
        label4.setText("By Hennessy")



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())