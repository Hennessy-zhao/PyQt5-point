#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

class MyWindow(QWidget):
    def keyPressEvent(self, evt):
        # QKeyEvent
        if evt.key()==Qt.Key_Tab:
            print("用户点击了Tab键位")

        #修饰键位 Ctrl并且 普通键位 s
        if evt.modifiers()==Qt.ControlModifier and evt.key()==Qt.Key_S:
            print("Ctrl+s被点击了")

        # 修饰键位 Ctrl+Shift并且 普通键位 s
        if evt.modifiers() == Qt.ControlModifier | Qt.ShiftModifier and evt.key() == Qt.Key_A:
            print("Ctrl+Shift+A被点击了")

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=MyWindow()
#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)

#如果想让label来捕获键盘事件
# label=QLabel(window)
# label.grabKeyboard()


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())