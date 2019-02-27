# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # em=QErrorMessage(self)
        # em.setWindowTitle("错误提示")
        # em.showMessage("社会我石姐，人狠话不多")
        # em.showMessage("社会我石姐，人狠话不多")
        # em.showMessage("社会我石姐，人狠话不多")
        # # em.exec_()
        # em.open()
        pass


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()

    #展示级别信息
    QErrorMessage.qtHandler()
    # qDebug("xxx")
    qWarning("123")


    sys.exit(app.exec_())