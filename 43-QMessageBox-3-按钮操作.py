# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        mb=QMessageBox(self)

        # mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)             #设置标准按钮

        #添加按按钮
        btn=QPushButton("xx1",mb)
        mb.addButton(btn,QMessageBox.YesRole)
        mb.addButton(QPushButton("xx2",mb),QMessageBox.NoRole)
        btn2= mb.addButton('xx3',QMessageBox.YesRole)

        # print(btn)
        # print(btn2)

        #移除按钮
        # mb.removeButton(btn)
        # mb.removeButton(btn2)

        #设置默认按钮
        # mb.setDefaultButton(btn2)

        #退出按钮（按ESC触发的按钮）
        # mb.setEscapeButton(btn2)


        # yes_btn=mb.buttons(QMessageBox.Yes)
        # no_btn=mb.buttons(QMessageBox.No)

        def test(btns):
            # print(btns)
            # if btns==btn2:
            #     print("点击了第二个按钮")
            # else:
            #     print("点击了第一个按钮")

            #识别标准按钮
            # if btns==yes_btn:
            #     print("点击了yes按钮")
            # else:
            #     print("点击了no按钮")

            #根据按钮性质来识别按钮
            role=mb.buttonRole(btns)
            if role==QMessageBox.YesRole:
                print("确认按钮被点击")
            else:
                print("取消按钮被点击")
            pass

        mb.buttonClicked.connect(test)

        mb.open()

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())