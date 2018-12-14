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
# window.setVisible(True)

btn=QPushButton(window)
btn.setText("按钮")

# print(btn.isHidden())
# print(btn.isVisible())      #如果第15行的window.setVisible(True)被注释掉，j结果会不一样

# btn.setVisible(False)           #设置之后，下一行为False
print(btn.isVisibleTo(window))      #父控件如果显示的时候，子空间是否跟着被显示


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())