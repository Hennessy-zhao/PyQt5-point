# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlaimText")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        pte=QPlainTextEdit(self)
        self.pte=pte
        pte.resize(300,300)
        pte.move(100,100)
        # self.占位提示文本()
        # self.只读设置()
        # self.格式设置()
        # self.软换行()
        # self.覆盖模式()
        # self.Tab控制()

        self.文本操作()

        test_btn=QPushButton(self)
        test_btn.move(20,20)
        test_btn.setText("按钮")
        test_btn.clicked.connect(self.btn_test)

    def 占位提示文本(self):
        self.pte.setPlaceholderText("请输入你的个人信息")
        print(self.pte.placeholderText())
        pass

    def 只读设置(self):
       # self.pte.setReadOnly(True)
        print(self.pte.isReadOnly())

    def 格式设置(self):
        tcf=QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(200,100,100))
        self.pte.setCurrentCharFormat(tcf)

    def 软换行(self):
        print(self.pte.lineWrapMode())      #查看换行默认情况
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)                 #设置为不自动换行

    def 覆盖模式(self):
        print(self.pte.overwriteMode())
        self.pte.setOverwriteMode(True)             #设置为覆盖模式
        print(self.pte.overwriteMode())

    def Tab控制(self):
        self.pte.setTabChangesFocus(False)       #改变焦点
        self.pte.setTabStopDistance(100)

    def 文本操作(self):
        # self.pte.setPlainText("社会社会，哈哈哈")
        self.pte.insertPlainText("www.baidu.com")
        self.pte.appendPlainText("<a href='www.baidu.com'>www.baidu.com</a>")
        self.pte.appendHtml("<a href='www.baidu.com'>www.baidu.com</a>")

    def 块操作(self):
        print(self.pte.blockCount())                #块即段落
        self.pte.setMaximumBlockCount(3)            #设置最大块数
        print(self.pte.toPlainText())               #打印文本
        pass

    def btn_test(self):
        # self.块操作()
        # self.放大缩小()
        # self.滚动保证光标可见()
        self.光标操作()

    def 放大缩小(self):
        self.pte.zoomIn(2)

    def 滚动保证光标可见(self):
        # self.pte.centerCursor()         #令光标出现位置在中间位置
        self.pte.ensureCursorVisible()      #保证光标可见（移动的是最小距离）
        self.pte.setFocus()
        pass

    def 光标操作(self):
        self.pte.setCursorWidth(20)             #设置光标宽度
        self.pte.setCursorWidth(20)             #设置光标宽度
        tc=self.pte.textCursor()            #获取光标对象
        # tc.insertImage('images/1.png')                  #用QTextEdit才能显示
        #tc.insertTable(5,3)                                #用QTextEdit才能显示

        tc1=self.pte.cursorForPosition(QPoint(100,60))
        # print(tc1)

        self.pte.moveCursor(QTextCursor.End,QTextCursor.KeepAnchor)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())