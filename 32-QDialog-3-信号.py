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

d=QDialog(window)
d.setWindowTitle("对话框")

btn1= QPushButton(d)
btn1.setText("btn1")
btn1.move(20,20)
btn1.clicked.connect(lambda :d.accept())

btn2= QPushButton(d)
btn2.setText("btn2")
btn2.move(60,60)
btn2.clicked.connect(lambda :d.reject())

btn3= QPushButton(d)
btn3.setText("btn3")
btn3.move(160,160)
btn3.clicked.connect(lambda :d.done(8))

d.accepted.connect(lambda :print("点击了接受按钮"))
d.rejected.connect(lambda :print("点击了拒绝按钮"))
d.finished.connect(lambda val:print("点击了完成按钮",val))

d.exec_()

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())