#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("内容边距设定")
window.resize(500,500)

label=QLabel(window)
label.setText("社会社会，哈哈哈")
label.resize(300,300)
label.setStyleSheet("background-color:cyan;")

label.setContentsMargins(100,200,0,0)       #设置边距，设置的分别是：左、上、右、下 四个方向


print(label.contentsRect())     #内容展示区域的大小


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())