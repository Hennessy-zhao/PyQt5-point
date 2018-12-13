#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()      #调用父类的方法
        pixmap = QPixmap("./images/cusor.png").scaled(50, 50)
        cusor = QCursor(pixmap)
        self.setCursor(cusor)

        # 2.2 设置控件
        self.setWindowTitle("鼠标操作案例")
        self.resize(500, 500)
        # 设置鼠标跟踪
        self.setMouseTracking(True)

        self.label = QLabel(self)
        self.label.setText("社会社会")
        self.label.move(100, 100)
        self.label.setStyleSheet("background-color:red")

    def mouseMoveEvent(self, mv):
        # print("鼠标移动")
        # label=self.findChild(QLabel)
        self.label.move(mv.localPos().x(),mv.localPos().y())     #也可以写成label.move(mv.x(),mv.y())


#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=MyWindow()





#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())