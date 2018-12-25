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

text=QTextEdit(window)

#文本内容发生改变
def text_change():
    print("文本内容发生改变")

#文本选中的内容发生改变
def selection_change():
    print("文本选中的内容发生改变")

#复制是否可用

def copy_a(yes):
    print("复制是否可用",yes)

text.textChanged.connect(text_change)
text.selectionChanged.connect(selection_change)
text.copyAvailable.connect(copy_a)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())