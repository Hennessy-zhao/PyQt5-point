#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QToolButton使用")
window.resize(500,500)

tb=QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon("./images/cusor.png"))     #如果同时显示文本和图标，则，自动显示图标
tb.setIconSize(QSize(50,50))
tb.setToolTip("这是一个新建按钮")


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())