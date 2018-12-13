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

window.move(100,100)
window.resize(200,200)

print(window.x())
print(window.width())
print(window.geometry())


#2.3 显示控件
window.show()

#等控件加载完毕之后再获取，否则就会像上面那样，出现错误的大小
print(window.x())
print(window.width())
print(window.geometry())

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())