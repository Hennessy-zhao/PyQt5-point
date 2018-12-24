#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)


btn=QPushButton("按钮",window)

btn.pressed.connect(lambda : print("press信号被触发"))
btn.released.connect(lambda : print("release信号被触发"))
btn.clicked.connect(lambda : print("click信号被触发"))
btn.toggled.connect(lambda : print("toggle信号被触发"))


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())