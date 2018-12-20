# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QText-Edit学习")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        self.text=QTextEdit(self)
        self.text.move(100,100)

        test_btn=QPushButton("按钮",self)
        test_btn.move(10,10)
        test_btn.clicked.connect(self.test)

        self.wenben()           #文本内容设置

        self.zhanwei()          #占位文本提示

    #文本内容的设置
    def wenben(self):
        #设置普通文本内容
        # self.text.setPlainText("<h1>社会社会</h1>")
        # self.text.insertPlainText("<h2>张三李四</2>")       #在光标位置处插入的，一打开，光标是在文本最前端
        # print(self.text.toPlainText())                      #获取文本

        # self.text.setHtml("<h1>社会社会</h1>")
        # self.text.insertHtml("<h2>Hennessy</h2>")
        # print(self.text.toHtml())                           #打印一个html4的模板

        self.text.setText("<h1>这是一个html文本</h1>")
        self.text.append("插入一个文本")          #在文本的最后追加一个文本


    #占位文本的提示
    def zhanwei(self):
        self.text.setPlaceholderText("请输入你的个人简介")

    #按钮点击测试
    def test(self):
        # self.text.clear()           #清空文本
        # print(self.text.document())         #获取文本文档
        # QTextDocument
        print(self.text.textCursor())
        QTextCursor

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())