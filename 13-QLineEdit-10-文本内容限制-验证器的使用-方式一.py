# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class AgeValidator(QValidator):
    def validate(self, input_str, pos_int):     #前面是输入的字符串，后面是光标位置
        print(input_str,pos_int)

        #判定
        #结果字符串，应该全部都是由一些数字组成
        #return
        try:

            if 18<=int(input_str)<=180:
                return (QValidator.Acceptable,input_str,pos_int)
            elif 1<=int(input_str)<=17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)         #返回无效状态，就不会被显示出来
            # return (QValidator.Acceptable, input_str, 1)          #这样光标位置一致都是1
        except:
            if len(input_str)==0:
                return (QValidator.Intermediate, input_str, pos_int)
            return(QValidator.Invalid,input_str,pos_int)

    def fixup(self, p_str):
        print("xxx",p_str)
        try:
            if int(p_str)<18:
                return "18"
            return "180"
        except:
            return "18"

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEdit")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        le=QLineEdit(self)
        le.move(100,100)
        #18-180

        validator=AgeValidator()
        le.setValidator(validator)

        le2=QLineEdit(self)
        le2.move(200,200)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())