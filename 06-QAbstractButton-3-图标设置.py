#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-图标设置")
window.resize(500,500)


btn=QPushButton(window)
btn.setText("按钮")
icon=QIcon('./images/cusor.png')
btn.setIcon(icon)
size=QSize(20,20)
btn.setIconSize(size)

print(btn.icon())       #获取按钮中的图标
print(btn.iconSize())   #获取按钮中图标的大小

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())