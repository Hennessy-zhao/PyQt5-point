#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

class Window(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("窗口操作-案例")
        self.resize(500, 500)

        self.setWindowFlag(Qt.FramelessWindowHint)  # 无边框，无标题栏
        self.setWindowOpacity(0.9)  # 设为半透明状态

        # 公共数据
        self.top_margin = 10
        self.btn_w = 80
        self.btn_h = 30

        self.setup_UI()

    def setup_UI(self):


        # 添加三个子空间-窗口的右上角
        close_btn = QPushButton(self)
        self.close_btn=close_btn
        close_btn.setText("关闭")
        close_btn.resize(self.btn_w, self.btn_h)

        max_btn = QPushButton(self)
        self.max_btn=max_btn
        max_btn.setText("最大化")
        max_btn.resize(self.btn_w, self.btn_h)

        mini_btn = QPushButton(self)
        self.mini_btn=mini_btn
        mini_btn.setText("最小化")
        mini_btn.resize(self.btn_w, self.btn_h)



        close_btn.pressed.connect(self.close)  # 用clicked也可以

        def max_normal():
            if window.isMaximized():
                window.showNormal()
                max_btn.setText("最大化")
            else:
                window.showMaximized()
                max_btn.setText("恢复")

        max_btn.pressed.connect(max_normal)
        mini_btn.pressed.connect(self.showMinimized)

    #窗口大小发生了改变自动执行该方法
    def resizeEvent(self, QResizeEvent):
        # close_btn_w=btn_w
        window_w = self.width()
        close_btn_x = window_w - self.btn_w
        close_btn_y = self.top_margin
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = self.top_margin
        self.max_btn.move(max_btn_x, max_btn_y)

        mini_btn_x = max_btn_x - self.btn_w
        mini_btn_y = self.top_margin
        self.mini_btn.move(mini_btn_x, mini_btn_y)

    def mousePressEvent(self, evt):
        #判定点击的是否是鼠标左键
        if evt.button()==Qt.LeftButton:
            #在此处设计一个标记，用作判定是否需要移动
            self.flag_move=True
            #一个是整个窗口的原始坐标点
            self.window_x=self.x()
            self.window_y=self.y()
            #鼠标按下的点
            self.mouse_x=evt.globalX()
            self.mouse_y=evt.globalY()

    def mouseMoveEvent(self, evt):
        # if 窗口的移动标记==True
            #根据鼠标按下的点，计算移动向量
            #根据移动量，和窗口的原始坐标=新的坐标
            #移动整个窗口的位置
        if self.flag_move==True:
            self.move_x=evt.globalX()-self.mouse_x
            self.move_y=evt.globalY()-self.mouse_y
            value_x=self.window_x+self.move_x
            value_y=self.window_y+self.move_y
            self.move(value_x,value_y)

    def mouseReleaseEvent(self, QMouseEvent):
        #把这个标记，进行重置 False
        self.flag_move=False
app=QApplication(sys.argv)

window=Window()

window.show()

sys.exit(app.exec_())