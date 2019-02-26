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
        # result=QFileDialog.getOpenFileName(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result=QFileDialog.getOpenFileNames(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result=QFileDialog.getOpenFileUrl(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result=QFileDialog.getOpenFileUrls(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")
        # result=QFileDialog.getSaveFileName(self,"选择一个py文件","./","All(*.*);;Images(*.png *.jpg);;Python文件(*.py)","Python文件(*.py)")


        # result=QFileDialog.getExistingDirectory(self,"选择一个文件夹","./")
        result=QFileDialog.getExistingDirectoryUrl(self,"选择一个文件夹",QUrl("./"))
        print(result)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())