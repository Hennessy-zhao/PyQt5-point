#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("父子关系学习")
window.resize(500,500)

label1=QLabel(window)
label1.setText("标签1")

label2=QLabel(window)
label2.setText("标签2")
label2.move(50,50)

label3=QLabel(window)
label3.setText("标签3")
label3.move(100,100)

print(window.childAt(55, 55))       #查看坐标(55,55)处是否有控件，并打印出控件
print(label2.parentWidget())        #查看label2的父控件

print(window.childrenRect())        #window的子空间组成的矩形区域



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())