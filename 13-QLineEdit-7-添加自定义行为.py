#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("添加自定义行为")
window.resize(500,500)

le=QLineEdit(window)
le.setEchoMode(QLineEdit.Password)

def change():
    # print("改变明文和密文")
    if le.echoMode()==QLineEdit.Password:
        le.setEchoMode(QLineEdit.Normal)
        action.setIcon(QIcon("./images/1.png"))
    else:
        le.setEchoMode(QLineEdit.Password)
        action.setIcon(QIcon("./images/2.png"))

#添加自定义行为操作（明文和密文的切换）
action=QAction(le)
action.setIcon(QIcon("./images/2.png"))
action.triggered.connect(change)
le.addAction(action,QLineEdit.TrailingPosition)     #放在外部
# le.addAction(action,QLineEdit.LeadingPosition)     #放在头部


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())