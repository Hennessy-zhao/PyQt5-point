#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("功能作用")
window.resize(500,500)

frame=QFrame(window)
frame.resize(100,100)
frame.move(100,100)
frame.setStyleSheet("background-color:cyan;")

# frame.setFrameShape(QFrame.Box)
# frame.setFrameShadow(QFrame.Raised)

frame.setFrameStyle(QFrame.Box | QFrame.Raised)     #一行代替上面两行


frame.setLineWidth(6)
frame.setMidLineWidth(12)           #中线在某些形状下无法显示

print(frame.frameWidth())           #打印线宽（外线+中线+内部一点部分）

frame.setFrameRect(QRect(20,20,60,60))         #框架矩形



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())