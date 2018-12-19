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

le_1=QLineEdit(window)


le_2=QLineEdit(window)
le_2.move(0,100)

btn=QPushButton("点击",window)
btn.move(200,0)

def cao():
    print(le_2.isModified())        #查看是否被编辑的状态
    le_2.setModified(False)         #设置被编辑状态为False

btn.clicked.connect(cao)

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())