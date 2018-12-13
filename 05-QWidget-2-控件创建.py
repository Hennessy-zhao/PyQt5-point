#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()        #按住ctrl键，鼠标左键点击查看QWidget类

red=QWidget(window)
red.resize(100,100)
red.setStyleSheet("background-color:red")

window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())