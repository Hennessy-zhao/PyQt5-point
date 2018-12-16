#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QLineEdit-功能测试")
window.resize(500,500)

# l1=QLineEdit("Hennessy",window)
l1=QLineEdit(window)
l1.setText("Hennessy")
# l1.insert("18")   #在之前的文本后面插入

btn=QPushButton(window)
btn.setText("按钮")
btn.move(100,100)
# btn.pressed.connect(lambda :l1.insert("22"))
btn.pressed.connect(lambda :print(l1.text()))

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())