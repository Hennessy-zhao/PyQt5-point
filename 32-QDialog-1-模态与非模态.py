#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QDialog")
window.resize(500,500)

d=QDialog(window)
d.setWindowTitle("对话框")
# d.exec_()         #当该种模态的对话框出现时，用户必须首先对对话框进行交互，直到关闭对话框，然后才能访问程序中其他的窗口
# d.open()          #该模态仅仅阻塞与对话框关联的窗口，但是依然允许用户与程序中其它窗口交互

# d.setModal(True)        #设置为模态，设置后当该种模态的对话框出现时，用户必须首先对对话框进行交互，直到关闭对话框，然后才能访问程序中其他的窗口
d.setWindowModality(Qt.WindowModal)         #设置为模态，和上一行代码作用相同

d.show()            #不会阻塞与对话框关联的窗口以及与其他窗口进行交互



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())