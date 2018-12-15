#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-快捷键")
window.resize(500,500)

btn=QPushButton(window)
btn.setText("按钮")
# btn.setText("按钮（&b）")       #按快捷键Alt+a则按钮被点击
btn.setShortcut("Alt+B")

btn.clicked.connect(lambda : print(1))


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())