# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("控件交互案例")
        self.resize(500,500)

        self.setup_ui()

    def setup_ui(self):
        #添加三个子空间
        label=QLabel(self)
        label.setText("登陆成功")
        label.move(100,50)
        label.hide()

        le=QLineEdit(self)
        le.setText("")
        le.move(100,100)

        btn=QPushButton(self)
        btn.setText("登录")
        btn.move(100,150)
        btn.setEnabled(False)

        def text_cao(text):
            # if len(text)>0:
            #     btn.setEnabled(True)
            # else:
            #     btn.setEnabled(False)
            btn.setEnabled(len(text)>0)
            # print("text发生了改变:"+text)
        le.textChanged.connect(text_cao)

        def check():
            # print("按钮被点击了")
            #获取文本框内容
            content=le.text()
            #判断是否是Hennessy内容
            # 是：显示之前隐藏的提示标签，显示文本
            if content=='Hennessy':
                # label.setVisible(True)
                label.setText("登录成功")
            else:
                label.setText("登录失败")
            label.show()



        btn.clicked.connect(check)


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())