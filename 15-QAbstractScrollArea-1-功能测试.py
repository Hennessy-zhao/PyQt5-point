#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QTextEdit父类功能测试")
window.resize(500,500)

text=QTextEdit("Hennessy",window)
text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)           #始终显示滚动条        Qt.ScrollBarAlwaysOff   始终不显示滚动条    Qt.ScrollBarAsNeeded  当内容太大而不适合时，QAbstractScrollArea显示滚动条。
text.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

#显示滚动条角落控件
btn=QPushButton(window)
btn.setIcon(QIcon("./images/cusor.png"))
text.setCornerWidget(btn)

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())