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
        # layout.addRow(sex_label, h_layout)
        layout.addRow(age_label,age_sb)
        layout.addRow(submit_btn)

        #插入行
        layout.insertRow(2,"性别",h_layout)

        # print(layout.rowCount())                #行数
        # print(layout.getWidgetPosition(age_sb))         #获取控件位置  第一个参数表示行，第二个参数表示是左边还是右边
        # print(layout.getLayoutPosition(h_layout))         #获取控件位置

        #移除行
        # layout.removeRow(1)           #移除一整行，需要用setParent(None)来释放
        # print(layout.takeRow(1))        #移除不删除，需要隐藏
        # age_label.hide()
        # age_sb.hide()

        #标签操作
        # print(layout.labelForField(name_le).setText("xxx"))         #修改标签

        #行包装策略
        layout.setRowWrapPolicy(QFormLayout.WrapLongRows)           #标签被赋予足够的水平空间以适合最宽的标签，其余的空间被赋予字段。标签被赋予足够的水平空间以适合最宽的标签，其余的空间被赋予字段。

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())