#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-排他性")
window.resize(1000,1000)

for i in range(0,3):
    btn=QPushButton(window)
    btn.setText("btn"+str(i))
    btn.move(50*i,50*i)

    # print(btn.autoExclusive())      #查看排他性是True还是False
    # print(btn.isCheckable())            #全部是False，要设置排他性，首先要令所有按钮的isCheckable为True
    btn.setCheckable(True)
    btn.setAutoExclusive(True)      #设置排他性，按钮只能一个被选中

btn=QPushButton(window)     #这个按钮和上面的三个按钮不是相互排斥的
btn.setCheckable(True)
btn.setText("btn3")
btn.move(250,250)

for i in range(0,3):
    btn=QRadioButton(window)
    btn.setText("btn"+str(i))
    btn.move(300+50*i,300+50*i)

    # print(btn.autoExclusive())
    # print(btn.isCheckable())
    btn.setAutoExclusive(False)     #设置排他性，设置为False，则这三个按钮不排他，可以同时被选中


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())