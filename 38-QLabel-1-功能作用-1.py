# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # label=QLabel("Hennessy",self)
        # label=QLabel("<h1>xxx</h1>",self)
        # label=QLabel("账号(&s)",self)
        label = QLabel("<a href='www.baidu.com'>百度</a>", self)
        label.setStyleSheet("background-color:cyan")
        label.move(100,100)
        label.resize(150,300)
        # label.adjustSize()

        # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        # label.setIndent(20)         #一般是左侧和右侧有缩进
        label.setMargin(20)

        # label.setTextFormat(Qt.PlainText)

        le1=QLineEdit(self)
        le1.move(250,250)
        label.setBuddy(le1)             #点击快捷键Alt+S，焦点调到le1

        le2 = QLineEdit(self)
        le2.move(250, 300)

        #内容（图片）缩放
        # label.setPixmap(QPixmap("./images/cusor.png"))
        # label.adjustSize()
        # label.setScaledContents(True)

        #文本交互
        # label.setTextInteractionFlags(Qt.TextSelectableByMouse |Qt.TextSelectableByKeyboard | Qt.TextEditable)             #可以用鼠标来选中，也可以用键盘来选中，也可以编辑

        #选中文本
        # label.setSelection(0,2)     #选中的字符

        # 链接
        # label.setOpenExternalLinks(True)

        #单词换行
        label.setWordWrap(True)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())