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
        pte = QPlainTextEdit(self)
        self.pte = pte
        pte.resize(300, 300)
        pte.move(100, 100)

        test_btn = QPushButton(self)
        test_btn.move(20, 20)
        test_btn.setText("按钮")
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        self.信号操作()

    def 信号操作(self):
        # self.pte.textChanged.connect(lambda :print("内容发生了改变"))
        # self.pte.selectionChanged.connect(lambda :print("选中内容发生了改变",self.pte.textCursor().selectedText()))
        # self.pte.modificationChanged.connect(lambda val:print("修改状态发生了改变",val))
        # doc=self.pte.document()
        # doc.setModified(False)      #改变编辑状态

        self.pte.blockCountChanged.connect(lambda val:print("块的个数发生了改变",val))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())