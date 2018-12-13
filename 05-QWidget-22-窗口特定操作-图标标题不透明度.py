#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("图标标题不透明度")
window.resize(500,500)

#设置图标
icon=QIcon('./images/cusor.png')
window.setWindowIcon(icon)

print(window.windowIcon())

#设置标题
window.setWindowTitle("图标标题不透明度")
print(window.windowTitle())

#设置透明度
window.setWindowOpacity(0.7)
print(window.windowOpacity())


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())