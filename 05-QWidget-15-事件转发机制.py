#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys


class MyWindow(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("顶层窗口被按下")

class MidWindow(QWidget):
    def mousePressEvent(self, QMouseEvent):
        print("中间控件被按下")

class Label(QLabel):

    #如果下面的被注释，即没有对Label控件进行鼠标点击事件的操作，那么会自动传递给MidWindow，如果上一层还是没有处理，再往上传递
    #如果在Label里面处理了mousePressEvent，那么他的父对象就不会再处理这个事件
    def mousePressEvent(self, evt):
        print("标签控件被按下")
        # evt.accept()
        print(evt.isAccepted())     #判断该事件是否被接收处理
        #意为令事件被忽视，不处理。则会将该事件被转发到父类
        # evt.ignore()

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=MyWindow()
#2.2 设置控件
window.setWindowTitle("事件转发")
window.resize(500,500)

mid_Window=MidWindow(window)
mid_Window.resize(300,300)
mid_Window.setAttribute(Qt.WA_StyledBackground,True)
mid_Window.setStyleSheet("background-color:yellow")


label=Label(mid_Window)
label.setText("这是一个标签")
label.move(100,100)
label.setStyleSheet("background-color:red")

btn=QPushButton(mid_Window)
btn.setText("我是按钮")
btn.move(50,50)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())