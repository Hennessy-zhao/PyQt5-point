#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("窗口状态")
window.resize(500,500)
#window.setWindowState(Qt.WindowActive)

print(window.windowState() == Qt.WindowNoState)     #查看目前窗口状态是否是无状态
window.show()
#设置窗口状态
#window.setWindowState(Qt.WindowMaximized)   #Qt.WindowMaximized 最大化  Qt.WindowMinimized 最小化  Qt.WindowFullScreen  全屏  Qt.WindowActive 活动窗口  Qt.WindowNoState 无状态

window2=QWidget()
window2.setWindowTitle("2")
window2.setWindowState(Qt.WindowActive)      #活动窗口状态
window2.show()





#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())