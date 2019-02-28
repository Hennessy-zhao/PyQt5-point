# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        mb=QMessageBox(self)
        mb.setWindowTitle("消息提示")
        # mb.setIcon(QMessageBox.Information)     #标准图标

        mb.setIconPixmap(QPixmap("images/1.png").scaled(20,20))         #自定义图标

        # mb.setTextFormat(Qt.PlainText)              #修改文本格式

        mb.setText("<h3>文件内容已经被修改</h3>")                 #主标题

        mb.setInformativeText("<h4>是否直接关闭，不保存</h4>")             #副标题

        mb.setCheckBox(QCheckBox("下次不再提醒",mb))                      #复选框

        mb.setDetailedText("你修改的内容是给每行代码加了一个分号")            #详情文本，不支持富文本

        mb.open()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())