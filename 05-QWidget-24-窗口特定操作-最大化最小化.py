#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys


class MyWindow(QWidget):
    #当点击界面，最大化显示，再点击，正常显示
    def mousePressEvent(self, QMouseEvent):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=MyWindow()
#2.2 设置控件
window.setWindowTitle("窗口操作-最大化最小化")
window.resize(500,500)


#2.3 显示控件
window.show()

#window.showMaximized()      #界面最大化显示
#window.showMinimized()      #界面最小化显示



#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())