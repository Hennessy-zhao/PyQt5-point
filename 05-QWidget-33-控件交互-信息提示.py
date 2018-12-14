#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QMainWindow()

#懒加载：用到的时候才会创建
window.statusBar()

#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)
window.setWindowFlags(Qt.WindowContextHelpButtonHint)       #先设置窗口状态后面的设置label.setWhatsThis("这是啥？这是标签")才会有用

#当鼠标停留在窗口控件身上之后，在状态栏提示的一段文本
window.setStatusTip("这是窗口")


label=QLabel(window)
label.setText("Hennessy制作")
label.setStatusTip("这是标签")
label.setToolTip("这是标签")
label.setToolTipDuration(2000)  #这个提示出现的时间
print(label.toolTipDuration())      #获取提示出现的时间


label.setWhatsThis("这是啥？这是标签")  #点击问号按钮之后再点击标签，会出现：这是啥？这是标签



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())