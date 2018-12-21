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
        #光标插入
        # self.guangbiao_insert()

        #设置格式合并
        # self.geshi_shezhihebing()

        #内容格式获取
        self.huoqu_neironggeshi()

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
        '''
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
        '''

        '''插入框架'''
        tc=self.text.textCursor()
        tff=QTextFrameFormat()
        tff.setBorder(10)
        tff.setBorderBrush(QColor(100,50,50))
        tff.setRightMargin(50)
        tc.insertFrame(tff)                 #插入一个框架

        doc=self.text.document()            #框架里面再做一些事情
        root_frame=doc.rootFrame()
        root_frame.setFrameFormat(tff)

    '''设置和合并格式'''
    def geshi_shezhihebing(self):
        tc=self.text.textCursor()

        '''设置要格式化的当前块（或选择中包含的所有块）的块char 格式'''
        '''
        tcf=QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(20)
        tcf.setFontOverline(True)       #上划线
        tcf.setFontUnderline(True)      #下划线
        tc.setBlockCharFormat(tcf)
        '''


        '''设置当前块的块格式（或选择中包含的所有块）以进行格式化'''
        '''
        tbf=QTextBlockFormat()
        tbf.setIndent(3)            #缩进
        tbf.setAlignment(Qt.AlignCenter)        #中间对齐
        tc.setBlockFormat(tbf)
        '''


        '''将光标的当前字符格式设置为给定格式。如果光标有选择，则给定格式应用于当前选择'''
        '''
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(20)
        tcf.setFontOverline(True)  # 上划线
        tcf.setFontUnderline(True)  # 下划线
        tc.setBlockCharFormat(tcf)
        tc.setCharFormat(tcf)
        '''


        '''合并当前字符格式'''
        tbf=QTextCharFormat()
        tbf.setFontStrikeOut(True)          #设置删除线
        tc.mergeCharFormat(tbf)

    '''内容和格式获取'''
    def huoqu_neironggeshi(self):
        tc=self.text.textCursor()

        #获取光标所在的文本块
        # print(tc.block().text())            #QTextBlock

        #获取光标所在的文本块编号
        # print(tc.blockNumber())

        #获取当前所在的文本列表

        #先创建一个文本列表
        # tlf = QTextListFormat()
        # tlf.setIndent(3)  # 缩进
        # tlf.setNumberPrefix("<<")  # 前缀     前缀和后缀只有在下面style设置为数字的时候才会显示
        # tlf.setNumberSuffix(">>")  # 后缀
        # tlf.setStyle(QTextListFormat.ListDecimal)
        # tl = tc.createList(tlf)

        print(tc.currentList())             #没有则为None




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())