# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Login_Pane import LoginPane
from Register_Pane import RegisterPane
from Caculator_Pane import CaculatorPane

import sys


if __name__=='__main__':
    app=QApplication(sys.argv)
    login_pane=LoginPane()
    register_pane = RegisterPane(login_pane)
    register_pane.move(0, login_pane.height())
    register_pane.show()

    caculator_pane = CaculatorPane()

    def show_register_pane():
        # print("展示注册界面")
        animation=QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0,login_pane.height()))
        animation.setEndValue(QPoint(0,0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def exit_register_pane():
        animation = QPropertyAnimation(register_pane)
        animation.setTargetObject(register_pane)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(login_pane.width(),0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def check_login(account,pwd):
        if account=="834819108" and pwd=="123456":
            print("登陆成功")

            caculator_pane.show()
            login_pane.hide()

        else:
            #登录失败，要求一个动画效果
            # print("失败")
            login_pane.show_error_animation()

    #信号的链接
    login_pane.show_register_pane_signal.connect(show_register_pane)
    login_pane.check_login_signal.connect(check_login)
    register_pane.register_account_pwd_signal.connect(lambda account,pwd:print(account,pwd))
    register_pane.exist_signal.connect(exit_register_pane)



    login_pane.show()
    sys.exit(app.exec_())