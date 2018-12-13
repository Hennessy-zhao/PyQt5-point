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
window.move(200,200)

#总控件个数
widget_count=100
#一行多少列
column_count=3

#计算一个控件一个控件的宽度
widget_width=window.width()/column_count
#总共多少行(编号//一行多少列  +1)
row_count=(widget_count-1)//column_count +1
#每个控件高度
widget_height=window.height()/row_count

for i in range(0,widget_count):
    w=QWidget(window)
    w.resize(widget_width,widget_height)
    widget_x=(i%column_count)*widget_width
    widget_y=(i//column_count)*widget_height
    w.move(widget_x,widget_y)
    w.setStyleSheet("background-color:red")




#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())