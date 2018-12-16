#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QCheckBox")
window.resize(500,500)

# QCheckBox
cb=QCheckBox("Python",window)
cb.setIcon(QIcon("./images/cusor.png"))
cb.setIconSize(QSize(30,30))
cb.setShortcut("Alt+P")     #设置快捷键

#设置是否支持三态
cb.setTristate(True)

#设置状态
# cb.setChecked(True)
cb.setCheckState(Qt.PartiallyChecked)

# Qt.Unchecked
# 	该项目未选中
# Qt.PartiallyChecked
# 	部分选中
# Qt::Checked
# 	真的被选中

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())