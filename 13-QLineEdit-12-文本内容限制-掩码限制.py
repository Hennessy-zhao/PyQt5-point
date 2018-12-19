#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("掩码")
window.resize(500,500)

le=QLineEdit(window)

#设置掩码
#总共输入5位字符，左边2（必须是大写字母）-右边2（必须是一个数字）
# le.setInputMask(">AA-99")
le.setInputMask(">AA-99;#")   #意为，如果没输入，以井号键显示。也可以不用#用其他字符


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())