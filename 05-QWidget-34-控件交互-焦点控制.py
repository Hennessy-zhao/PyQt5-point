#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

class Window(QWidget):
    def mousePressEvent(self, evt):     #鼠标点击控件以外的空白区域才有效
        print(self.focusWidget())
        # self.focusNextChild()       #鼠标点击光标到下一个控件
        # self.focusPreviousChild()   #鼠标点击光标到上一个控件
        # self.focusNextPrevChild(True)       #True是鼠标点击光标到下一个控件，False#鼠标点击光标到上一个控件



#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=Window()
#2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500,500)

le1=QLineEdit(window)
le1.move(50,50)

le2=QLineEdit(window)
le2.move(100,100)

le3=QLineEdit(window)
le3.move(150,150)

#设置控件获取焦点的顺序是1,3,2
QWidget.setTabOrder(le1,le3)
QWidget.setTabOrder(le3,le2)

# le2.setFocus()      #给第二个控件设置焦点
# le2.setFocusPolicy(Qt.TabFocus)         #第二个只能能通过Tab键获取焦点，用其他方式获取不到
# le2.setFocusPolicy(Qt.ClickFocus)           #只能通过鼠标点击获取焦点
# le2.setFocusPolicy(Qt.StrongFocus)          #可以通过鼠标和Tab键获取焦点
# le2.setFocusPolicy(Qt.NoFocus)              #不可用鼠标点击和Tab键获取焦点，只能用setFocus获取
# le2.clearFocus()                            #不让这个标签获取焦点

#获取当前窗口内容，所有子控件当中获取焦点的那个控件
# print(window.focusWidget())             #打印的是None     如果是先把一个焦点设置为setFocus，窗口打开才会出现控件名


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())