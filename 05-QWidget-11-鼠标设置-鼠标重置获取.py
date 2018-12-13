#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("鼠标重置")
window.resize(500,500)

window.setCursor(Qt.ForbiddenCursor)

#使鼠标形状恢复原状
# window.unsetCursor()

#鼠标获取
print(window.cursor())

current_cursor=window.cursor()
print(current_cursor.pos())     #获取鼠标的位置
current_cursor.setPos(100,100)      #设置鼠标的位置


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())