# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")

        self.setup_ui()

    def setup_ui(self):
        pass



if __name__=='__main__':
    app=QApplication(sys.argv)


    '''例子1'''

    # win1=QWidget()
    # win1.setStyleSheet("background-color:red;")
    # win1.show()
    #
    # win2 = QWidget()
    # win2.setStyleSheet("background-color:green;")
    # win2.resize(200,200)        #如果win2超过win1的大小，也不会超出，就完全覆盖掉win1而已
    # win2.setParent(win1)
    # win2.show()


    '''例子2'''
    win_root=QWidget()

    label1=QLabel(win_root)
    label1.setText("111")

    label2 = QLabel(win_root)
    label2.setText("222")
    label2.move(200,200)

    label3 = QLabel(win_root)
    label3.setText("333")
    label3.move(300,300)

    for labels in win_root.findChildren(QLabel):
        labels.setStyleSheet("color:red")

    win_root.show()

    sys.exit(app.exec_())