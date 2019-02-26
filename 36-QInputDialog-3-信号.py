# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        inputd=QInputDialog(self)

        # inputd.setInputMode(QInputDialog.IntInput)
        # inputd.intValueChanged.connect(lambda val:print("整形数据发生改变",val))
        # inputd.intValueSelected.connect(lambda val:print("整形数据最终被选中",val))

        # inputd.setInputMode(QInputDialog.DoubleInput)
        # inputd.doubleValueChanged.connect(lambda val:print("浮点形数据发生改变",val))
        # inputd.doubleValueSelected.connect(lambda val:print("浮点形数据最终被选中",val))

        inputd.setComboBoxItems(["abc", "def", "lalala"])

        inputd.setInputMode(QInputDialog.TextInput)
        inputd.textValueChanged.connect(lambda val: print("字符串数据发生改变", val))
        inputd.textValueSelected.connect(lambda val: print("字符串数据最终被选中", val))

        inputd.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())