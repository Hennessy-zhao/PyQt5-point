#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("文本的设置和获取")
window.resize(500,500)

le_a=QLineEdit(window)
le_a.move(100,200)

le_b=QLineEdit(window)
le_b.move(100,300)

copy_btn=QPushButton(window)
copy_btn.setText("复制")
copy_btn.move(100,400)

def copy_cao():
    #1.获取文本框内容a的内容
    content=le_a.text()
    #2.把上面获取到的内容，设置到文本框B里面
    le_b.setText(content)       #如果用insert就是不清除文本框B，而是在B的文本基础上继续


copy_btn.clicked.connect(copy_cao)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())