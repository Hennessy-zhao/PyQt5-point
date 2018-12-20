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
        self.text=QTextEdit(self)
        self.text.move(100,100)

        btn=QPushButton("按钮",self)
        btn.move(10,10)
        btn.clicked.connect(self.btn_test)

    def btn_test(self):
        self.guangbiao_insert()

    #光标插入内容
    def guangbiao_insert(self):
        '''插入文本内容'''
        '''
        tcf=QTextCharFormat()
        tcf.setToolTip("网址")
        tcf.setFontFamily("微软雅黑")
        tcf.setFontPointSize(55)

        tc = self.text.textCursor()
        tc.insertText("哈哈哈",tcf)

        tc.insertHtml("<a href='www.baidu.com'>百度</a>")
        
        '''

        '''插入图片'''
        '''
        tif=QTextImageFormat()
        tif.setName("./images/cusor.png")
        tif.setWidth(100)
        tif.setHeight(100)
        tc=self.text.textCursor()
        tc.insertImage(tif)
        # tc.insertImage(tif,QTextFrameFormat.FloatRight)     #后一个参数是设置位置
        # tc.insertImage("./images/cusor.png")
        '''

        '''插入文本片段（句子）'''
        '''
        # tif=QTextDocumentFragment.fromHtml("<h1>Hello Word</h1>")
        tif=QTextDocumentFragment.fromPlainText("<h1>Hello Word</h1>")
        tc = self.text.textCursor()
        tc.insertFragment(tif)
        '''

        '''插入列表'''
        '''
        tc=self.text.textCursor()
        # tl=tc.insertList(QTextListFormat.ListCircle)
        # tl=tc.insertList(QTextListFormat.ListDecimal)
        # tl=tc.createList(QTextListFormat.ListDecimal)
        # print(tl)

        tlf=QTextListFormat()
        tlf.setIndent(3)        #缩进
        tlf.setNumberPrefix("<<")       #前缀     前缀和后缀只有在下面style设置为数字的时候才会显示
        tlf.setNumberSuffix(">>")       #后缀
        tlf.setStyle(QTextListFormat.ListDecimal)
        tl=tc.createList(tlf)
        '''

        '''插入表格'''
        '''
        ttf=QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        ttf.setCellPadding(6)
        ttf.setCellSpacing(13)
        # 设置列宽，是一个可迭代的对象，设置每一列的列宽,50代表50%
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength,50),QTextLength(QTextLength.PercentageLength,40),QTextLength(QTextLength.PercentageLength,10)))

        tc=self.text.textCursor()
        print(tc.insertTable(5, 3, ttf))
        table=tc.insertTable(5,3,ttf)         #可以打印出来，是一个对象  QTextTable类
        # table.appendColumns(2)              #使用的是QTextTable对应的方法
        '''

        '''插入文本块（段落）'''
        tc=self.text.textCursor()
        tc.insertBlock()            #插入一个空的文本块
        self.text.setFocus()

        tbf=QTextBlockFormat()
        tbf.setAlignment(Qt.AlignRight)
        tbf.setRightMargin(100)
        tbf.setIndent(3)        #缩进

        tcf=QTextCharFormat()
        tcf.setFontFamily("微软雅黑")
        tcf.setFontItalic(True)     #字体倾斜
        tcf.setFontPointSize(20)
        # tc.insertBlock(tbf)            #设置文本块格式
        tc.insertBlock(tbf,tcf)            #设置文本块格式 和 文本格式

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())