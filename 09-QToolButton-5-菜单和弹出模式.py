#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("菜单和弹出模式")
window.resize(500,500)

tb=QToolButton(window)
tb.setText("工具")
tb.setIcon(QIcon('./images/cusor.png'))
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
tb.setAutoRaise(True)

# btn=QPushButton(window)
# btn.setText("一般按钮")
# btn.move(100,100)
# btn.setFlat(True)

menu=QMenu(tb)
# menu.setTitle("菜单")

sub_menu=QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon('./images/cusor.png'))

action=QAction(QIcon("./images/cusor.png"),"行为",menu)
action.triggered.connect(lambda :print("点击了菜单选项"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action)

tb.clicked.connect(lambda :print("工具按钮被点击了"))       #下方 不同的菜单弹出模式，对于菜单的点击反应是不一样的


tb.setMenu(menu)
#如果不设置弹出方式，鼠标按住一会才显示
#设置弹出方式
# tb.setPopupMode(QToolButton.MenuButtonPopup)            #有一个专门的指示箭头
tb.setPopupMode(QToolButton.InstantPopup)            #点击按钮之后立刻出现


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())