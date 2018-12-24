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
# text.copy()     #复制文本
# text.paste()    #粘贴
# text.selectAll()    #全选
#查找
text.find("xx",QTextDocument.FindBackward)      #向后查找，如果不放，就是向前查找       QTextDocument.FindCaseSensitively   #区分大小写     QTextDocument.FindWholeWords    #使查找匹配仅完整的单词。


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())