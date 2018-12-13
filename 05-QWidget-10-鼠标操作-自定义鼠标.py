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

label=QLabel(window)
label.setText("社会社会")
label.resize(200,200)
label.setStyleSheet("background-color:red")
# label.setCursor(Qt.ForbiddenCursor)

pixmap=QPixmap('./images/cusor.png')
new_pixmap=pixmap.scaled(50,50)     #scaled是一个返回值，需要有一个变量来接受这个参数
cursor=QCursor(new_pixmap,0,0)      #后面的两个0是修改鼠标的热点，即这个鼠标的0,0位置作为鼠标点击有效的位置
label.setCursor(cursor)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())