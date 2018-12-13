#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#方法一：自定义类别
'''
class Label(QLabel):
    def mousePressEvent(self, QMouseEvent):
        self.setStyleSheet("background-color:red")
'''

#方法二

class Window(QWidget):
    def mousePressEvent(self, evt):
        # QMouseEvent
        local_x=evt.x()
        local_y=evt.y()
        sub_widget=self.childAt(local_x,local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color:red")

#2.控件的操作
#2.1 创建控件
window=Window()
#2.2 设置控件
window.setWindowTitle("父子关系案例")
window.resize(500,500)

for i in range(1,11):
    label=QLabel(window)
    label.setText('标签'+str(i))
    label.move(i*40,i*40)

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())
