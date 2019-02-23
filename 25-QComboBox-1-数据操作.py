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
        cb=QComboBox(self)
        cb.resize(400,30)
        # cb.addItem("xx1")
        # cb.addItem(QIcon("images/1.png"),"xx2")
        # cb.addItems(["1","2","3"])
        # cb.addItems(("4","5","6"))
        #
        # cb.insertItem(1,"xxx")
        #
        # cb.setItemIcon(3,QIcon("images/2.png"))
        # cb.setItemText(4,"Hennessy")
        # cb.removeItem(5)
        #
        # cb.insertSeparator(2)       #插入分割线
        #
        # cb.setCurrentIndex(1)               #设置当前显示的字
        # cb.setCurrentText("xxx")
        #
        # cb.setEditable(True)            #当前控件可被编辑
        # cb.setEditText("lalala")

        #模型操作
        print(QAbstractItemModel.__subclasses__())
        model=QStandardItemModel()
        item1=QStandardItem("item1")
        item2=QStandardItem("item2")
        item22=QStandardItem("item22")
        item2.appendRow(item22)
        model.appendRow(item1)
        model.appendRow(item2)
        cb.setModel(model)

        cb.setView(QTreeView(cb))



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())