# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from resource.caculator_ui import Ui_Form
import sys

class Caculator(QObject):

    def __init__(self,parent):
        super().__init__(parent)

        #数字键位 num 运算符 operator
        self.key_models=[]

    def parse_key_model(self,key_model):
        # print(key_model)
        if key_model["role"]=="clear":
            print("清空所有内容")
            return None

        if key_model["role"]=="caculate":
            print("计算所有内容")
            return None
        #num operator
        if len(self.key_models)==0:
            if key_model["role"]=="num":
                if key_model["title"]==".":
                    key_model["title"]="0."
                self.key_models.append(key_model)
            return None

        if key_model["role"]==self.key_models[-1]["role"]:
            if key_model["role"]=="num":
                if key_model["title"]=="." and self.key_models[-1]["title"].__contains__("."):
                    return None

                if self.key_models[-1]["title"]!="0":
                    self.key_models[-1]["title"]+=key_model["title"]
                else:
                    self.key_models[-1]["title"] = key_model["title"]

            if key_model["role"]=="operator":
                self.key_models[-1]["title"] = key_model["title"]

        else:
            self.key_models.append(key_model)

        print(self.key_models)

class CaculatorPane(QWidget,Ui_Form):

    show_register_pane_signal=pyqtSignal()
    check_login_signal=pyqtSignal(str,str)

    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)

        self.setAttribute(Qt.WA_StyledBackground,True)              #设置之后背景图片才会出现

        self.setupUi(self)
        self.caculator=Caculator(self)


    def get_key(self,title,role):
        # print(title,role)
        self.caculator.parse_key_model({"title":title,"role":role})

if __name__=='__main__':
    app=QApplication(sys.argv)

    form=CaculatorPane()


    form.show()

    sys.exit(app.exec_())