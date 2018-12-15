#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-自动重复")
window.resize(500,500)

def cao():
    num=int(btn.text())+1
    btn.setText(str(num))

btn=QPushButton(window)
btn.setText("1")
btn.clicked.connect(cao)


btn.setAutoRepeat(True)     #设置按钮自动重复
btn.setAutoRepeatInterval(1000)        #设置自动重复时间间隔
btn.setAutoRepeatDelay(1000)            #按下按钮延迟1s之后触发事件

print(btn.autoRepeat())     #检测是否自动重复
print(btn.autoRepeatInterval())     #检测自动重复时间间隔
print(btn.autoRepeatDelay())        #检测按钮点击后延迟多少时间自动重复


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())