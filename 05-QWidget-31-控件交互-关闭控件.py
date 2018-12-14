#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("交互状态")
window.resize(500,500)

btn=QPushButton(window)
btn.setText("按钮")

btn.destroyed.connect(lambda : print("按钮被释放了"))

btn.setAttribute(Qt.WA_DeleteOnClose,True)      #意思是，当btn.close()时候，按钮被释放了，会打印;按钮被释放了。这两行是结合起来一起用的
btn.close()     #关闭控件，按钮隐藏，不被绘制。但是没有被释放，所以不会打印：按钮被释放了

# btn.deleteLater()   #按钮被释放


#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())