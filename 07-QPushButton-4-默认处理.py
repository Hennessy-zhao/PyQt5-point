#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-默认处理")
window.resize(500,500)

btn1=QPushButton("按钮1",window)
btn2=QPushButton("按钮2",window)
btn2.move(100,100)

# btn2.setAutoDefault(True)       #是要用户点击了这个按钮之后，才会把它设置为默认按钮
btn2.setDefault(True)               #不需要用户点击，也会自从设置为默认按钮

print(btn1.autoDefault())
print(btn2.autoDefault())


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())