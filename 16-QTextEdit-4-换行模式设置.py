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
#软换行模式
# text.setLineWrapMode(QTextEdit.NoWrap)      #没有软换行, 超过宽度后, 会产生水平滚动条

# text.setLineWrapMode(QTextEdit.FixedPixelWidth)      #填充像素宽度，和下面一行配合
# text.setLineWrapColumnOrWidth(100)

# text.setLineWrapMode(QTextEdit.FixedColumnWidth)      #填充像素宽度，和下面一行配合
# text.setLineWrapColumnOrWidth(8)                    #固定列

text.setWordWrapMode(QTextOption.WordWrap)            #设置单词换行模式，保持单词完整性


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())