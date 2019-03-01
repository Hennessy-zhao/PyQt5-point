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
        name_label = QLabel("姓名(&n)：")
        age_label = QLabel("年龄(&g)：")

        name_le = QLineEdit()
        age_sb = QSpinBox()

        # 设置小伙伴
        name_label.setBuddy(name_le)
        age_label.setBuddy(age_sb)

        sex_label = QLabel("性别")
        male_rb = QRadioButton("男")
        female_rb = QRadioButton("女")
        h_layout = QHBoxLayout()
        h_layout.addWidget(male_rb)
        h_layout.addWidget(female_rb)

        submit_btn = QPushButton("提交")

        # 1.创建布局管理器
        layout = QFormLayout()

        # 2.把布局管理器赋值给需要布局的父控件
        self.setLayout(layout)

        #修改行
        layout.setWidget(0,QFormLayout.LabelRole,name_label)
        layout.setWidget(0,QFormLayout.FieldRole,name_le)

        layout.setLayout(1,QFormLayout.FieldRole,h_layout)




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())