#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("交互状态[*]")        #如果界面被编辑状态，这个*会出现，*也可以放在其他位置。只能用[*]，其他符号都不可以
window.resize(500,500)

window.setWindowModified(True)              #设置文件状态为被编辑状态




#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())