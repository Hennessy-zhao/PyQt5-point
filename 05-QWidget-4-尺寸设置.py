#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("尺寸设置")
window.resize(500,500)      #修改的是用户区域的宽和高
window.setFixedSize(500,500)        #设置固定值之后，就不能再用拖动的方式去改变窗口的大小

window.move(0,0)


label=QLabel(window)
label.setText("社会")
label.move(100,100)
label.setStyleSheet("background-color:cyan")

def changeCao():
    new_content=label.text()+"社会"
    label.setText(new_content)
    # label.resize(label.width()+100,label.height())
    label.adjustSize()      #令label的大小自适应label内容的大小

btn=QPushButton(window)
btn.setText("增加内容")
btn.move(100,300)
btn.clicked.connect(changeCao)




#2.3 显示控件
window.show()

#window.setGeometry(0,0,150,150)  #设置的是用户区域距离左上角的位置，要在显示之后再设置

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())