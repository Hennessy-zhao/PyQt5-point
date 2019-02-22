# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

#子类化类
class MyASB(QAbstractSpinBox):
    def __init__(self,parent=None,num="0",*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.lineEdit().setText(num)

    def stepEnabled(self):
        #限定0-9

        current_num=int(self.text())
        if current_num==0:
            return QAbstractSpinBox.StepUpEnabled
        elif current_num==9:
            return QAbstractSpinBox.StepDownEnabled
        elif current_num<0 or current_num>9:
            return QAbstractSpinBox.StepNone
        else:
            return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        current=int(self.text())+p_int
        self.lineEdit().setText(str(current))

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QABstractSpinBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # asb=QAbstractSpinBox(self)
        asb=MyASB(self)
        # asb=MyASB(self,2)
        asb.resize(100,30)
        asb.move(100,100)



if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())