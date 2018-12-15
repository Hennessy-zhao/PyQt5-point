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

btn=QCommandLinkButton("标题","描述",window)        #一个扁平化的按钮
# btn.setText("标题2")        #修改标题
# btn.setDescription("第二个描述")   #修改描述
# btn.setIcon(QIcon('./images/cusor.png'))

print(btn.description())        #获取描述

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())