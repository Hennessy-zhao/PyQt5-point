from PyQt5.Qt import *
import  sys

class Btn(QPushButton):
    #重写函数，设置有效区域
    def hitButton(self, point):
        # print(point)       #输出点击的位置
        #做一个判定，只有点击按钮的右半部分，才会有反应
        # if point.x()>self.width()/2:
        #     return True     #返回True表示点有效，返回False表示点击无效，连接的槽函数也不会生效


        # 做一个判定，只有点击按钮的内切圆，才会有效，否则无效
        #通过给定的一个点坐标，计算与圆心的距离
        #如果距离<半径，True，否则False
        yuanxin_x=self.width()/2
        yuanxin_y=self.height()/2

        hit_x=point.x()
        hit_y=point.y()

        #((x1-x2)^2+(y1-y2)^2)开平方
        diatance= math.sqrt(math.pow(hit_x-yuanxin_x,2)+math.pow(hit_y-yuanxin_y,2))

        if diatance<self.width()/2:
            return True

        return False

    def paintEvent(self, evt):
        super().paintEvent(evt)     #在父类绘制的基础上，再绘制下面的。或者用painter.drawText()重新绘制
        painter=QPainter(self)
        painter.setPen(QPen(QColor(100,0,0),6))
        painter.drawEllipse(self.rect())
        # painter.drawText(100,100,self.text())

