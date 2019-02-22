# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeysequence")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        kse=QKeySequenceEdit(self)
        # ks=QKeySequence("Ctrl+C")
        # ks=QKeySequence(QKeySequence.Copy)
        ks=QKeySequence(Qt.CTRL+Qt.Key_C,Qt.CTRL+Qt.Key_A)           #枚举法
        kse.setKeySequence(ks)
        # kse.clear()             #清空

        btn=QPushButton(self)
        btn.move(100,100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda :print(kse.keySequence().toString(),kse.keySequence().count()))

        kse.editingFinished.connect(lambda :print("结束编辑"))
        kse.keySequenceChanged.connect(lambda key_val:print("键位序列发生改变",key_val.toString()))
        


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())