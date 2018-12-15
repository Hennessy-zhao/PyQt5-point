#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-模拟点击")
window.resize(500,500)

btn=QPushButton(window)
btn.setText("这是个按钮")
btn.move(200,200)
btn.clicked.connect(lambda : print("按钮被点击了"))

# btn.animateClick(2000)      #模拟按钮被点击，在2s之后被点击的

btn2=QPushButton(window)
btn2.setText("按钮2")
def test():
    #btn.click()             #按钮没有一个可视的被按下的反应
    btn.animateClick(1000)  #按钮会有一个可视的被按下的反应
btn2.clicked.connect(test)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())