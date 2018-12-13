# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("信号与槽机制")

        self.setup_ui()

    def setup_ui(self):
        self.test_QObject()

    def test_QObject(self):
        self.obj=QObject()
        # obj.destroyed
        # obj.objectNameChanged

        def destroy_cao(obj):
            print("对象被释放了",obj)

        def obj_name_cao(objName):
            print("对象名称发生了变化",objName)

        self.obj.destroyed.connect(destroy_cao)
        self.obj.objectNameChanged.connect(obj_name_cao)

        self.obj.setObjectName("111")

        self.obj.objectNameChanged.disconnect()         #取消控件链接，则objectNameChanged()不会被触发，则obj_name_cao()不会被执行
        self.obj.setObjectName("222")

        self.obj.objectNameChanged.connect(obj_name_cao)
        self.obj.blockSignals(True)     #临时阻断信号与槽的链接

        print(self.obj.signalsBlocked(),"1")    #检测是否被阻断

        self.obj.setObjectName("333")

        self.obj.blockSignals(False)

        print(self.obj.signalsBlocked(), "2")  # 检测是否被阻断

        self.obj.setObjectName("444")

        print(self.obj.receivers(self.obj.objectNameChanged))       #检测当前有多少个槽函数被连接了
                                                                    #只连接了一个槽函数obj_name_cao，所以下面self.obj.receivers(self.obj.objectNameChanged)输出的是1

        del  self.obj




if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())