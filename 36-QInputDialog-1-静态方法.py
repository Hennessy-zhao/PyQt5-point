# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # result=QInputDialog.getInt(self,"xx1","xxx2",888,step=8)
        # result=QInputDialog.getDouble(self,"xx1","xxx2",888.88,decimals=2)
        # result=QInputDialog.getText(self,"xx1","xx2",echo=QLineEdit.Password)
        # result=QInputDialog.getMultiLineText(self,"xx1","xx2","Hennessy")
        result=QInputDialog.getItem(self,"xx1","xx2",["Hennessy","Eligah","Gin","Rye"],2,True)
        print(result)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())