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

        sex_label = QLabel("性别：")
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

        # 3.把需要布局的子控件交给布局管理器进行布局
        layout.addRow(name_label, name_le)
        layout.addRow(sex_label, h_layout)
        layout.addRow(age_label, age_sb)
        layout.addRow(submit_btn)

        #对齐方式
        # print(layout.formAlignment() == Qt.AlignLeft | Qt.AlignTop)
        layout.setFormAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        layout.setLabelAlignment(Qt.AlignRight)

        layout.setVerticalSpacing(20)       #竖直方向间距
        layout.setHorizontalSpacing(30)     #水平方向间距

        #字段增长策略
        layout.setFieldGrowthPolicy(QFormLayout.FieldsStayAtSizeHint)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())