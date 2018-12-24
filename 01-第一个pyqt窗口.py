# -*- coding:UTF-8 -*-
from PyQt5.Qt import *          #导入需要的包
import sys

app=QApplication(sys.argv)      #创建一个应用程序

#创建控件，设置控件
window=QWidget()
window.setWindowTitle("第一个PyQt窗口")
window.resize(500,500)
window.move(300,300)

label=QLabel(window)
label.setText("第一个窗口")
label.move(200,200)

#展示控件
window.show()

#开始执行程序，并进入消息循环
#保证整个程序不会退出
#检测整个程序所接收到的用户的交互信息
sys.exit(app.exec_())

