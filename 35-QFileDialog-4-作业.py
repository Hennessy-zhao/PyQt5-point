# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog作业")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        #获取文件中信息
        def get_text(val):
            # print(val)
            file=open(val,'r')

            content=file.read()

            text.setPlainText(content)

            file.close()

        #保存新文件
        def save_text(val):
            url=val

            content=text.toPlainText()

            file = open(val, 'w')

            file.write(content)

            file.close()


        #打开文件按钮被点击
        def open_file():
            file=QFileDialog(self)

            file.fileSelected.connect(get_text)

            file.open()

        #保存文件按钮被点击
        def save_file():
            file=QFileDialog(self)

            file.setAcceptMode(QFileDialog.AcceptSave)
            file.fileSelected.connect(save_text)

            file.open()


        btn_open=QPushButton(self)
        btn_open.move(100,50)
        btn_open.setText("打开文件")
        btn_open.clicked.connect(open_file)

        btn_save = QPushButton(self)
        btn_save.move(300, 50)
        btn_save.setText("保存文件")
        btn_save.clicked.connect(save_file)

        text=QTextEdit(self)
        text.resize(300,300)
        text.move(100,100)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())