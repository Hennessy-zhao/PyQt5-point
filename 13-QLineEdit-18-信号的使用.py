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

le=QLineEdit(window)
le.move(100,100)

le_2=QLineEdit(window)
le_2.move(300,100)

def cao():
    pass

le.textEdited.connect(lambda val:print("文本编辑的时候",val))              #用户在编辑的时候，而不是开发人员设置text的
le.textChanged.connect(lambda val:print("文本内容发生变化的时候",val))
# le.setText("xxx")       #指出发了第二个，不触发第一个

le.returnPressed.connect(lambda :le_2.setFocus())           #回车键被按下的时候
le.editingFinished.connect(lambda :print("结束编辑"))

le.cursorPositionChanged.connect(lambda old_pos,new_pos:print(old_pos,new_pos))         #光标发生变化的时候，第一个参数是旧光标位置，第二个参数是新光标位置

le.selectionChanged.connect(lambda :print("选中文本发生改变",le.selectedText()))        #选中的文本发生变化的时候


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())