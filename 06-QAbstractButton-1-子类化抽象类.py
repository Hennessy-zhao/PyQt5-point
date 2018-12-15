#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QAbstractButton")
window.resize(500,500)

class Btn(QAbstractButton):
    def paintEvent(self, evt):
        # print("重新绘制这个按钮")
        #绘制按钮需要展示的一个界面内容
        #可以暂时看不懂
        #1.创建一个画家，画画在哪里
        painter=QPainter(self)      #括号里传的值可以类比成画布
        #2.给画家一个笔
        #2.1创建一个笔
        pen=QPen(QColor(0,0,255),20)      #参数为笔的颜色和宽度
        #2.2设置这个笔
        painter.setPen(pen)

        #3.画家画画
        painter.drawText(20,20,self.text())        #参数为绘画的位置和内容
        painter.drawEllipse(50,50,200,200)       #画椭圆，参数是一个矩形

# btn=QAbstractButton(window)     #这是不对的，无法通过该类创建出一个控件，应该子类化，即写一个类来继承他
btn=Btn(window)
btn.setText("按钮")
btn.resize(500,500)

btn.clicked.connect(lambda :print("点击了这个按钮"))

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())