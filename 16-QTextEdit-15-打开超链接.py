#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


class MyTextEdit(QTextEdit):
    def mousePressEvent(self, m1):
        # print(m1.pos())
        link_str=self.anchorAt(m1.pos())
        if len(link_str)>0:
            QDesktopServices.openUrl(QUrl(link_str))
        return super().mousePressEvent(m1)

#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("")
window.resize(500,500)

text=MyTextEdit(window)
text.insertHtml("xxx"*300+"<a name='www.baidu.com' href='www.baidu.com'>撩妹</a>"+"aaa"*200)      #name是重点，获取的是name的值



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())