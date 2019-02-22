# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        dte=QDateTimeEdit(QDateTime.currentDateTime(),self)
        # dte=QDateTimeEdit(QDate.currentDate(),self)
        # dte=QDateTimeEdit(QTime.currentTime(),self)
        dte.move(100,100)
        dte.setDisplayFormat("yy-MM-dd | m : ss : zzz")

        btn=QPushButton(self)
        btn.move(200,200)
        btn.setText("测试")
        def test():
            # dte.setFocus()
            # dte.setCurrentSectionIndex(3)
            # dte.setCurrentSectionIndex(QDateTimeEdit.MinuteSection)
            # print(dte.sectionText(QDateTimeEdit.MinuteSection))

            #日期范围
            # dte.setMaximumDateTime(QDateTime(2020,8,15,12,30))
            # dte.setMinimumDateTime(QDateTime(1900,1,1,0,0))
            # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3),QDateTime.currentDateTime().addDays(3))

            #是否弹出日历
            dte.setCalendarPopup(True)

            #获取时间
            print(dte.dateTime())
            print(dte.date())
            print(dte.time())

        btn.clicked.connect(test)

        #sectionCount() -> int
        #获取section个数
        # print(dte.sectionCount())

        #setCurrentSectionIndex(int)
        #设置当前的section索引

        # currentSectionIndex() -> int
        # 获取section索引
        # setCurrentSection(QDateTimeEdit.Section)
        # 设置当前操作的日期时间section
        # currentSection() -> QDateTimeEdit.Section
        # 获取当前的section部分
        # sectionAt(index_int) -> QDateTimeEdit.Section
        # 获取指定索引位置的section
        # sectionText(QDateTimeEdit.Section) -> str
        # 获取指定section的文本内容


        #信号
        dte.dateTimeChanged.connect(lambda val:print(val))
        dte.dateChanged.connect(lambda val:print("日期发生改变",val))
        dte.timeChanged.connect(lambda val:print("时间发生改变",val))


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())