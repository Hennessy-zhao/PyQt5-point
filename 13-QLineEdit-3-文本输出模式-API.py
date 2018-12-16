#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("文本输出模式")
window.resize(500,500)

le=QLineEdit(window)
le.setEchoMode(QLineEdit.Password)
print(le.echoMode())        #查看文本输出模式

    # NoEcho = 1
	# 不输出
    # Normal = 0
	# 正常输出
    # Password = 2
	# 密文形式
    # PasswordEchoOnEdit = 3
	# 编辑时明文, 结束后密文


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())