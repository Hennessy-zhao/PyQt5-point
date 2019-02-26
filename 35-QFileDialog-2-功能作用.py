# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):

        def test():
            fd=QFileDialog(self,'选择一个文件','../',"All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")
            fd.fileSelected.connect(lambda file:print(file))

            # fd.setAcceptMode(QFileDialog.AcceptSave)                #控制是选择一个文件还是保存一个文件
            # fd.setDefaultSuffix('txt')

            # fd.setFileMode(QFileDialog.Directory)           #切换模式，选择文件还是文件夹

            # fd.setNameFilter("IMG(*.jpg *.png *.jpeg)")             #设置过滤
            # fd.setNameFilters(["All(*.*)","Images(*.png *.jpg)","Python文件(*.py)"])

            # fd.setViewMode(QFileDialog.Detail)          #代码调试反应不大

            fd.setLabelText(QFileDialog.FileName,"Hennessy的文件")
            fd.setLabelText(QFileDialog.Accept,"Hennesy的接受")
            fd.setLabelText(QFileDialog.Reject,"Hennesy的拒绝")

            fd.open()

        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100,100)
        btn.clicked.connect(test)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())