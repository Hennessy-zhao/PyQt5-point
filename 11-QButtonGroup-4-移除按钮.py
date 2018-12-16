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

#男女
r_male=QRadioButton("男",window)
r_female=QRadioButton("女",window)
r_male.move(100,100)
r_female.move(100,150)
r_male.setChecked(True)

sex_group=QButtonGroup(window)
sex_group.addButton(r_male,1)
sex_group.addButton(r_female,2)

#移除按钮，从关系上移除，但是界面上不会消失
sex_group.removeButton(r_female)



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())