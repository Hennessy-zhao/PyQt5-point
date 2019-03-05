# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from resource.register_ui import Ui_Form
import sys

class RegisterPane(QWidget,Ui_Form):

    exist_signal=pyqtSignal()

    register_account_pwd_signal=pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

        self.setAttribute(Qt.WA_StyledBackground,True)              #设置之后背景图片才会出现

        self.setupUi(self)

        self.animation_targets=[self.about_menu_btn,self.reset_menu_btn,self.exit_menu_btn]
        self.animation_targets_pos=[target.pos() for target in self.animation_targets]

    def show_hide_menu(self,checked):
        print("显示和隐藏",checked)

        animation_group=QSequentialAnimationGroup(self)

        for idx,target in enumerate(self.animation_targets):
            animation=QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.main_menu_btn.pos())
                animation.setEndValue(self.animation_targets_pos[idx])
            else:
                animation.setStartValue(self.animation_targets_pos[idx])
                animation.setEndValue(self.main_menu_btn.pos())
            animation.setDuration(200)
            animation.setEasingCurve(QEasingCurve.OutBounce)            #弹簧弹出效果
            animation_group.addAnimation(animation)

        # animation_group.setDirection(checked)               #也可以用下面的if else语句实现
        # if not checked:
        #     animation_group.setDirection(QAbstractAnimation.Forward)       #正着执行
        # else:
        #     animation_group.setDirection(QAbstractAnimation.Backward)       #倒着执行

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)



    def about_lk(self):
        QMessageBox.about(self,"Hennessy","HennessyLaLaLa")
        print("关于")

    def reset(self):
        self.account_le.clear()
        self.password_le.clear()
        self.confirm_pwd_le.clear()
        print("重置")

    def exit_pane(self):
        # print("退出")
        self.exist_signal.emit()

    def check_register(self):
        # print("注册")
        self.register_account_pwd_signal.emit(self.account_le.text(),self.password_le.text())


    def enable_register_btn(self):
        # print("判定")
        account_txt=self.account_le.text()
        password_txt=self.password_le.text()
        cp_txt=self.confirm_pwd_le.text()

        if len(account_txt)>0 and len(password_txt)>0 and len(cp_txt)>0 and password_txt==cp_txt:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)



if __name__=='__main__':
    app=QApplication(sys.argv)

    form=RegisterPane()

    form.exist_signal.connect(lambda :print("退出"))

    form.register_account_pwd_signal.connect(lambda account,password:print(account,password))

    form.show()

    sys.exit(app.exec_())