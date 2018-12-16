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

le=QLineEdit(window)
le.setClearButtonEnabled(True)      #输入内容之后，自动显示一个按钮，点击之后，文本框所有内容消失
print(le.isClearButtonEnabled())    #查看该输入框是否有自动清除的按钮


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())