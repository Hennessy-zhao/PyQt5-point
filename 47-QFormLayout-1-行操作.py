# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFormLayout")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        name_label=QLabel("姓名(&n)：")
        age_label=QLabel("年龄(&g)：")

        name_le=QLineEdit()
        age_sb=QSpinBox()

        #设置小伙伴
        name_label.setBuddy(name_le)
        age_label.setBuddy(age_sb)

        sex_label=QLabel("性别")
        male_rb=QRadioButton("男")
        female_rb=QRadioButton("女")
        h_layout=QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn=QPushButton("提交")

        # 1.创建布局管理器
        layout=QFormLayout()

        # 2.把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        # 3.把需要布局的子控件交给布局管理器进行布局
        # layout.addWidget(name_label)
        # layout.addWidget(name_le)

        #添加行
        layout.addRow(name_label,name_le)
        #layout.addRow("姓名(&n)",name_le)     #也可以起到设置小伙伴的功效
        layout.addRow(sex_label, h_layout)
        layout.addRow(age_label,age_sb)
        layout.addRow(submit_btn)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())