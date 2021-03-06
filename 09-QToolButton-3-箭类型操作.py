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

btn=QToolButton(window)
btn.setArrowType(Qt.UpArrow)        #设置成向上箭头

# Qt.NoArrow
# 	无箭头
# Qt.UpArrow
# 	向上箭头
# Qt.DownArrow
# 	向下箭头
# Qt.LeftArrow
# 	向左箭头
# Qt.RightArrow
# 	向右箭头


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())