# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCalendarWidget")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        cw=QCalendarWidget(self)
        # cw.setSelectedDate(QDate(-9999,1,1))
        # cw.setMinimumDate(QDate(1990,1,1))
        # cw.setMaximumDate(QDate(2020,12,12))
        cw.setDateRange(QDate(1990,1,1),QDate(2020,12,12))

        # cw.setDateEditEnabled(False)
        # cw.setDateEditAcceptDelay(3000)         #延迟3000毫秒

        #日期获取
        btn=QPushButton(self)
        btn.setText("测试按钮")
        btn.move(400,400)
        # btn.clicked.connect(lambda :print(cw.monthShown()))
        # btn.clicked.connect(lambda :print(cw.yearShown()))
        # btn.clicked.connect(lambda :print(cw.selectedDate()))

        #格式外观
        # cw.setNavigationBarVisible(False)           #导航条是否可见
        cw.setFirstDayOfWeek(Qt.Sunday)                 #一周的第一天
        cw.setGridVisible(True)                         #设置网格

        #文本格式变化
        tcf=QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontPointSize(16)
        tcf.setFontUnderline(True)
        cw.setHeaderTextFormat(tcf)

        # cw.setHorizontalHeaderFormat(QCalendarWidget.LongDayNames)

        t_tcf=QTextCharFormat()
        t_tcf.setFontPointSize(20)
        t_tcf.setToolTip("这是星期二")
        # cw.setWeekdayTextFormat(Qt.Tuesday,t_tcf)

        # cw.setDateTextFormat(QDate(2019,2,27),t_tcf)


        # cw.setSelectionMode(QCalendarWidget.NoSelection)            #无法通过鼠标选中日期
        # cw.setSelectedDate(QDate(2019,2,27))

        #常规操作
        # showToday()
        # showSelectedDate()
        # showNextYear()
        # showPreviousYear()
        # showNextMonth()
        # showPreviousMonth()
        # setCurrentPage(int year, int month)

        # btn.clicked.connect(cw.showToday)
        # btn.clicked.connect(cw.showSelectedDate)
        btn.clicked.connect(lambda :cw.setCurrentPage(2019,2))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())