#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-菜单设置")
window.resize(500,500)

btn=QPushButton(QIcon('./images/cusor.png'),"按钮",window)

menu=QMenu()
#子菜单 最近打开
#行为动作 新建 打开 分割线 退出

# new_action=QAction()
# new_action.setText("新建")
# new_action.setIcon(QIcon('./images/cusor.png'))


new_action=QAction(QIcon('./images/cusor.png'),"新建",menu)
open_action=QAction(QIcon('./images/cusor.png'),"打开",menu)
exit_action=QAction(QIcon('./images/cusor.png'),"退出",menu)

new_action.triggered.connect(lambda :print("新建文件"))
open_action.triggered.connect(lambda :print("打开文件"))
exit_action.triggered.connect(lambda :print("退出程序"))

open_recent_menu=QMenu(menu)
open_recent_menu.setTitle("最近打开")
open_recent_menu.setIcon(QIcon("./images/cusor.png"))

file_action=QAction("Python-GUI编程")
open_recent_menu.addAction(file_action)


menu.addAction(new_action)
menu.addAction(open_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(exit_action)

btn.setMenu(menu)

print(btn.menu())       #获取menu

#2.3 显示控件
window.show()

btn.showMenu()      #要在窗口展示之后再展示菜单

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())