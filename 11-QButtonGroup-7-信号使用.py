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
r_female.setChecked(True)

r_male.move(100,100)
r_female.move(100,150)

sex_group=QButtonGroup(window)
sex_group.addButton(r_male)
sex_group.addButton(r_female)

def test(val):
    # print(val)      #每次打印两个，因为单选有两个按钮的状态发生了变化
    print(sex_group.id(val))

# sex_group.buttonToggled.connect(test)
sex_group.buttonClicked.connect(test)      #按钮被按下的时候。
# sex_group.buttonClicked[int].connect(test)      #按钮被按下的时候。选择传参数为int

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())