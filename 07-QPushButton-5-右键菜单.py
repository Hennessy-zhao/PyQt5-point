#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#方法一，重写contextMenuEvent()方法

class Window(QWidget):
    #鼠标右键之后出现的菜单
    def contextMenuEvent(self,evt ):
        print("默认上下文菜单地阿偶雍这个方法")
        # QContextMenuEvent
        # print("展示菜单")
        #将07-QPushButton-2-菜单设置中的菜单复制到这里
        menu = QMenu(self)

        new_action = QAction(QIcon('./images/cusor.png'), "新建", menu)
        open_action = QAction(QIcon('./images/cusor.png'), "打开", menu)
        exit_action = QAction(QIcon('./images/cusor.png'), "退出", menu)

        new_action.triggered.connect(lambda: print("新建文件"))
        open_action.triggered.connect(lambda: print("打开文件"))
        exit_action.triggered.connect(lambda: print("退出程序"))

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")
        open_recent_menu.setIcon(QIcon("./images/cusor.png"))

        file_action = QAction("Python-GUI编程")
        open_recent_menu.addAction(file_action)

        menu.addAction(new_action)
        menu.addAction(open_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()
        menu.addAction(exit_action)

        menu.exec_(evt.globalPos())            #展示菜单,后面的参数是菜单展示的位置。这里的位置是全局的位置

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=Window()
#2.2 设置控件
window.setWindowTitle("按钮-右键菜单")
window.resize(500,500)

#方法二  用了方法二，方法一的重写方法就无法生效了。两个方法使用其一  个人感觉方法二反应时间比较短
def show_menu(point):
    print(point)            #这个坐标点是相对于界面的，不是相对于屏幕
    menu = QMenu(window)

    new_action = QAction(QIcon('./images/cusor.png'), "新建", menu)
    open_action = QAction(QIcon('./images/cusor.png'), "打开", menu)
    exit_action = QAction(QIcon('./images/cusor.png'), "退出", menu)

    new_action.triggered.connect(lambda: print("新建文件"))
    open_action.triggered.connect(lambda: print("打开文件"))
    exit_action.triggered.connect(lambda: print("退出程序"))

    open_recent_menu = QMenu(menu)
    open_recent_menu.setTitle("最近打开")
    open_recent_menu.setIcon(QIcon("./images/cusor.png"))

    file_action = QAction("Python-GUI编程")
    open_recent_menu.addAction(file_action)

    menu.addAction(new_action)
    menu.addAction(open_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()
    menu.addAction(exit_action)

    dest_point=window.mapToGlobal(point)        #把局部的点映射到桌面上的点
    menu.exec_(dest_point)  # 展示菜单,后面的参数是菜单展示的位置。这里的位置是全局的位置
window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())