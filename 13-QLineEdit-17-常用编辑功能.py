#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("常用编辑功能")
window.resize(500,500)

le=QLineEdit(window)
le.move(100,100)
le.setDragEnabled(True)             #是否可以拖拽

le_2=QLineEdit(window)
le_2.resize(50,50)
le_2.move(300,100)

btn=QPushButton("按钮",window)
btn.move(100,200)

def cao():
    # le.backspace()          #退格
    # le.del_()                   #删除
    # le.clear()                  #清除文本
    # le.copy()                   #复制

    # le.paste()                      #粘贴

    # le.setSelection(2,1)          #选中指定区间的文本
    # le.setSelection(0, len(le.text()))  # 选中所有
    le.selectAll()                  #选中所有
    # le.deselect()                       #取消选中
    print(le.hasSelectedText())         #判断当前是否有被选中的（需要用代码选中，手动不行）
    print(le.selectedText())            #获取选中的文本
    print(le.selectionStart())          #选中的开始位置
    print(le.selectionEnd())            #选中的结束位置
    print(le.selectionLength())         #选中的长度

    le.setFocus()



btn.clicked.connect(cao)




#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())