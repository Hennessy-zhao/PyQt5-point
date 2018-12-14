#注意事项：如果父控件没有被绘制，则子控件也不会被绘制。所以就算有时候传递的参数值为True也不一定可见


#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

class Window(QWidget):

    #绘制事件
    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)      #调用父类来绘制窗口


class Btn(QPushButton):
    # 绘制事件
    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)  # 调用父类来绘制窗口

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=Window()
#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)

btn=Btn(window)
# btn.setVisible(False)               #令按钮不可见，不被绘制
btn.setText("按钮")
btn.pressed.connect(lambda :btn.setVisible(False))      #点击之后窗口被隐藏，不再被绘制


#2.3 显示控件
# window.show()
# window.setVisible(True)
window.setHidden(False)     #设置为不隐藏，可以绘制    先绘制父控件，再绘制子空间。先打印窗口被绘制，在打印按钮被绘制

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())