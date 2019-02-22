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
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled

    def stepBy(self, p_int):
        current=int(self.text())+p_int
        self.lineEdit().setText(str(current))


    #验证重写方法
    def validate(self, p_str, p_int):
        #18-180
        num=int(p_str)
        if num<18:
            return (QValidator.Intermediate,p_str,p_int)
        elif num<=180:
            return (QValidator.Acceptable,p_str,p_int)
        else:
            return (QValidator.Invalid,p_str,p_int)

    #修复方法
    def fixup(self, p_str):
        print(p_str)
        return "18"

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
        self.asb=asb

        #功能作用

        # asb.setAccelerated(True)            #长按时是否加速
        # print(asb.isAccelerated())
        #
        # asb.setReadOnly(True)               #只允许用户通过步长调节器调节, 不能使用键盘输入
        # print(asb.isReadOnly())

        test_btn=QPushButton(self)
        test_btn.move(200,200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)


        #信号
        self.asb.editingFinished.connect(lambda :print("结束编辑"))

    def btn_test(self):
        # print(self.asb.text())
        # self.asb.lineEdit().setText("5")
        #
        # cl=QCompleter(["sz","123","18"],self.asb)
        # self.asb.lineEdit().setCompleter(cl)
        # # self.asb.lineEdit().setAlignment(Qt.AlignCenter)
        # self.asb.setAlignment(Qt.AlignCenter)               #设置对齐方式

        # #设置框架
        # print(self.asb.hasFrame())
        # self.asb.setFrame(False)
        #
        # #清空
        # self.asb.clear()

        # self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)                 #设置按钮（默认是有上下箭头，这里设置为没有按钮）
        pass

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())