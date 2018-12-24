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
#字符设置

tcf=QTextCharFormat()
tcf.setFontFamily("宋体")
tcf.setFontPointSize(20)
tcf.setFontCapitalization(QFont.Capitalize)                 #设置字体大小写，首字母大小写  QFont.MixedCase 这是正常的文本呈现选项，不应用大写更改。  QFont.AllUppercase 这会改变要以全大写类型呈现的文本。  QFont.AllLowercase 这会改变要以全小写类型呈现的文本。  QFont.SmallCaps 这会改变要以小型大写字母呈现的文本。  QFont.Capitalize 这会将要呈现的文本更改为每个单词的第一个字符作为大写字符。

tcf2=QTextCharFormat()
tcf2.setFontItalic(True)

text.setCurrentCharFormat(tcf)
text.mergeCurrentCharFormat(tcf2)       #合并格式，把第二个格式也合并过去


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())