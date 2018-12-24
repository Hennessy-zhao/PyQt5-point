#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("自动格式化")
window.resize(500,500)

text=QTextEdit(window)
#自动格式化
text.setAutoFormatting(QTextEdit.AutoBulletList)            #输入*自动变成列表格式化

# QTextEdit.AutoNone
# 	不要做任何自动格式化。
# QTextEdit.AutoBulletList
# 	自动创建项目符号列表（例如，当用户在最左侧列中输入星号（'*'）时，或在现有列表项中按Enter键。
# QTextEdit.AutoAll
# 	应用所有自动格式。目前仅支持自动项目符号列表。


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())