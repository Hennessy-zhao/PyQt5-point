# -*- coding:UTF-8 -*-
from PyQt5.Qt import *          #导入需要的包
import sys

app=QApplication(sys.argv)      #创建一个应用程序

window=QWidget()
window.setWindowTitle("第一个PyQt窗口")
window.resize(500,500)
window.move(300,300)

label=QLabel(window)
label.setText("第一个窗口")
label.move(200,200)


window.show()

sys.exit(app.exec_())       #开始执行程序，并进入消息循环

