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
le.setMaxLength(5)      #设置最大长度
print(le.maxLength())   #获取最大长度

le_2=QLineEdit(window)
le_2.setText("这是第二个文本框")
le_2.move(0,200)
le_2.setReadOnly(True)      #设置为只读


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())