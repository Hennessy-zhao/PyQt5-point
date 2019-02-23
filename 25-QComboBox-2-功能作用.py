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

        btn=QPushButton(self)
        btn.move(300,100)
        btn.setText("测试按钮")

        #常用数据获取

        # btn.clicked.connect(lambda :print(cb.count()))
        # btn.clicked.connect(lambda :print(cb.currentIndex()))
        # btn.clicked.connect(lambda :print(cb.currentText()))
        # btn.clicked.connect(lambda :print(cb.currentData()))
        # btn.clicked.connect(lambda :btn.setIcon(cb.itemIcon(cb.currentIndex())))
        #btn.clicked.connect(lambda dix=cb.count():print(cb.itemIcon(dix),cb.itemText(dix),cb.itemData(dix)))


        #数据限制
        # btn.clicked.connect(lambda :cb.addItem("at"))
        cb.setEditable(True)
        # cb.setMaxCount(6)               #最大存储个数
        # cb.setMaxVisibleItems(3)        #最大显示个数
        # cb.setDuplicatesEnabled(True)       #是否可重复
        #
        # cb.setFrame(False)          #是否有边框
        # cb.setIconSize(QSize(60,60))
        # cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)              #尺寸调整（按照最大选项调整）

        #清空
        # btn.clicked.connect(lambda :cb.clear())
        # btn.clicked.connect(lambda :cb.clearEditText())         #必须是可编辑状态下，才可以清空
        btn.clicked.connect(lambda: cb.showPopup())                 #弹出下拉框


        cb.setCompleter(QCompleter(["123","abc","aaa","bbb"]))          #完成器

        #验证器
        QValidator


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())