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

text=QTextEdit(window)


text.insertHtml("xxx"*300+"<a name='lk' href='#itlike'>撩妹</a>"+"aaa"*200)

btn=QPushButton("按钮",window)
btn.move(300,0)

def cao():
    text.scrollToAnchor("lk")           #滚动到锚点

btn.clicked.connect(cao)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())