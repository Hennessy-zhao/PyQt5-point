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

btn=QPushButton(window)
btn.move(100,100)
btn.setText("点击")
btn.pressed.connect(lambda :print("按钮被按下了"))
btn.released.connect(lambda :print("鼠标被释放了"))

btn.clicked.connect(lambda value:print("鼠标被点击了",value))     #value代表这个按钮是否是被选中的状态

# btn.toggled.connect(lambda value:print("按钮的选中状态发生了改变",value))       #一般来说只有单选框和多选框使用

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())