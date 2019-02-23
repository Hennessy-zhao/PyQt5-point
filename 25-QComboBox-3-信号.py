# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        cb.resize(200, 30)
        cb.addItems(["abc","1243","456"])
        cb.addItem(QIcon("images/1.png"),"Hennessy",{'name':"lalala"})

        cb.setEditable(True)

        # cb.activated[str].connect(lambda val:print("条目被激活",val))
        # cb.currentIndexChanged.connect(lambda val:print("当前索引发生改变",val))
        # cb.currentTextChanged.connect(lambda val:print("当前文本发生改变",val))
        # cb.editTextChanged.connect(lambda val:print("当前编辑文本发生改变",val))
        # cb.highlighted[int].connect(lambda val:print("当前编辑文本发生改变",val))
        cb.highlighted[str].connect(lambda val:print("当前编辑文本发生改变",val))




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())