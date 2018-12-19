#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("光标位置控制")
window.resize(500,500)

le=QLineEdit(window)
le.move(100,100)

btn=QPushButton(window)
btn.setText("按钮")
btn.move(100,200)

def cursor_move():
    # le.cursorBackward(False,2)          #向后(左)移动steps个字符     ,False代表不选中文本
    # le.cursorBackward(True, 2)            # 向后(左)移动steps个字符     ,True代表选中文本
    # le.cursorForward(True,3)              #向前(左)移动steps个字符     ,True代表选中文本
    # le.cursorForward(False,3)              #向前(左)移动steps个字符     ,False代表不选中文本

    # le.cursorWordBackward(True)               #向后(左)移动一个单词长度，单词以空格为界 True代表选中文本
    # le.cursorWordForward(True)              #向前(右)移动一个单词长度，单词以空格为界 True代表选中文本

    # le.home(True)                   #光标移动到行首
    # le.end(True)                      # 光标移动到行尾
    le.setCursorPosition(len(le.text())/2)          #设置光标位置
    print(le.cursorPosition())                      #获取光标位置
    print(le.cursorPositionAt(QPoint(100, 120)))        #获取指定坐标位置对应文本光标位置

    le.setFocus()

btn.clicked.connect(cursor_move)


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())