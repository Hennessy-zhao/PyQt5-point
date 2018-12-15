#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("工具按钮样式设置")
window.resize(500,500)

btn=QToolButton(window)
btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)     #文字显示在图标旁边

# Qt.ToolButtonIconOnly
# 	仅显示图标
# Qt.ToolButtonTextOnly
# 	仅显示文字
# Qt.ToolButtonTextBesideIcon
# 	文本显示在图标旁边
# Qt.ToolButtonTextUnderIcon
# 	文本显示在图标下方
# Qt.ToolButtonFollowStyle
# 	遵循风格

btn.setText("工具")
btn.setIcon(QIcon("./images/cusor.png"))


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())