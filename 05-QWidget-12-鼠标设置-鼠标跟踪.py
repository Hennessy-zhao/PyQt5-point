#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

class MyWindow(QWidget):
    def mouseMoveEvent(self, me):
        print("鼠标移动了")
        print(me.globalPos())
        print(me.localPos())


#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=MyWindow()
#2.2 设置控件
window.setWindowTitle("鼠标跟踪")
window.resize(500,500)

#设置鼠标跟踪
window.setMouseTracking(True)

print(window.hasMouseTracking())        #查看当前是否存在鼠标跟踪






#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())