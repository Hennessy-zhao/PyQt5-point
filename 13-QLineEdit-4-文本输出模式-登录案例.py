# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class AccountTool:

    ACCOUNT_ERROR=1
    PWS_ERROR=2
    SUCCESS=3
    @staticmethod
    def check_login(account,pwd):
        #把账号和密码发送给服务器，等待服务器返回结果
        if account!="Hennessy":
            return AccountTool.ACCOUNT_ERROR
        if pwd!="123456":
            return AccountTool.PWS_ERROR
        return AccountTool.SUCCESS

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("登录案例")
        self.resize(500,500)
        self.setMinimumSize(400,400)
        self.setup_ui()

    def setup_ui(self):

        #添加三个控件
        self.account_le=QLineEdit(self)
        self.pwd_le=QLineEdit(self)
        self.pwd_le.setEchoMode(QLineEdit.Password)     #设置输出模式为密文
        self.login_btn=QPushButton(self)
        self.login_btn.setText("登录")

        self.login_btn.clicked.connect(self.login_cao)

    def login_cao(self):
        #获取账号和密码信息
        account=self.account_le.text()
        pwd=self.pwd_le.text()

        state=AccountTool.check_login(account,pwd)

        if state == AccountTool.ACCOUNT_ERROR:
            print("账号错误")
            self.account_le.setText("")
            self.pwd_le.setText("")
            self.account_le.setFocus()

        if state == AccountTool.PWS_ERROR:
            print("密码错误")
            self.pwd_le.setText("")
            self.pwd_le.setFocus()
        if state==AccountTool.SUCCESS:
            print("登陆成功")


        # if account != "Hennessy":
        #     print("账号错误")
        #     self.account_le.setText("")
        #     self.pwd_le.setText("")
        #     self.account_le.setFocus()
        #     return None
        #
        # if pwd!="123456":
        #     print("密码错误")
        #     self.pwd_le.setText("")
        #     self.pwd_le.setFocus()
        #     return None
        #
        # print("登陆成功")

    #当窗口屏幕大小改变的时候
    def resizeEvent(self, evt):
        widget_w = 150
        widget_h = 40
        margin = 60

        self.account_le.resize(widget_w, widget_h)
        self.pwd_le.resize(widget_w, widget_h)
        self.login_btn.resize(widget_w, widget_h)

        x = (self.width() - widget_w) / 2

        self.account_le.move(x, self.height() / 5)
        self.pwd_le.move(x, self.account_le.y() + widget_h + margin)
        self.login_btn.move(x, self.pwd_le.y() + widget_h + margin)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())