#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QRadioButton-多组互斥")
window.resize(500,500)

red=QWidget(window)
red.resize(100,100)
red.move(50,50)
red.setStyleSheet("background-color:red")

green=QWidget(window)
green.resize(100,100)
green.move(150,150)
green.setStyleSheet("background-color:green")

rb_nan=QRadioButton("男-&Male",red)
rb_nan.move(10,10)

rb_nv=QRadioButton("女-&Femaal",red)
rb_nv.move(10,50)


rb_yes=QRadioButton("yes",green)
rb_yes.move(10,10)

rb_no=QRadioButton("no",green)
rb_no.move(10,50)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())