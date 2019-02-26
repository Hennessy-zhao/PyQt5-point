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
        fd = QFileDialog(self, '选择一个文件', '../', "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")

        # fd.currentChanged.connect(lambda path:print("当前路径字符串发生改变时",path))
        # fd.currentUrlChanged.connect(lambda path:print("当前路径QUrl发生改变时",path))
        # fd.directoryEntered.connect(lambda path:print("当前目录字符串进入时",path))
        # fd.directoryUrlEntered.connect(lambda path:print("当前目录Url进入时",path))
        # fd.filterSelected.connect(lambda path:print("当前名称过滤字符串被选中时",path))

        fd.setFileMode(QFileDialog.ExistingFiles)

        fd.fileSelected.connect(lambda val:print("单个文件被选中时-字符串",val))
        fd.filesSelected.connect(lambda val:print("多个文件被选中时-列表[字符串]",val))
        fd.urlSelected.connect(lambda val:print("单个文件被选中时-url",val))
        fd.urlsSelected.connect(lambda val:print("多个文件被选中时-列表[url]",val))

        fd.open()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())