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

w2=QWidget()
w2.show()

#2.3 显示控件
window.show()
print(w2.isActiveWindow())      #如果两个窗口的show()顺序做一定改变，则两个值的活跃状态转变
print(window.isActiveWindow())


#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())