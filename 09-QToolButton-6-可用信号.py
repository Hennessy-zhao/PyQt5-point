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


tb=QToolButton(window)
tb.setPopupMode(QToolButton.InstantPopup)            #点击按钮之后立刻出现
tb.setText("按钮")

menu=QMenu(tb)

sub_menu=QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon('./images/cusor.png'))

action1=QAction(QIcon("./images/cusor.png"),"行为1",menu)
action1.setData([1,2,3])

action2=QAction(QIcon("./images/cusor.png"),"行为2",menu)
action2.setData({"name":"Hennessy"})

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

tb.setMenu(menu)

def do_action(action):
    print("点击了行为",action.data())        #可以获取行为设置的Data

tb.triggered.connect(do_action)     #只有点击了action才触发


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())