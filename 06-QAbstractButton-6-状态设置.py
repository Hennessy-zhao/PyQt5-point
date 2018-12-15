#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("按钮-状态设置")
window.resize(500,500)

push_button=QPushButton(window)
push_button.setText("这是QPushButton")
push_button.move(100,100)

radio_button=QRadioButton(window)
radio_button.setText("这是RadioButton")
radio_button.move(100,150)

checkbox_button=QCheckBox(window)
checkbox_button.setText("这是checkbox")
checkbox_button.move(100,200)

push_button.setStyleSheet("QPushButton:pressed{background-color:red}")

#把三个按钮都设置为：按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox_button.setDown(True)

# print(push_button.isCheckable())            #False
# print(radio_button.isCheckable())           #True
# print(checkbox_button.isCheckable())        #True

push_button.setChecked(True)
radio_button.setChecked(True)
checkbox_button.setChecked(True)

# print(push_button.isChecked())
# print(radio_button.isChecked())
# print(checkbox_button.isChecked())

def cao():
    radio_button.toggle()
    checkbox_button.toggle()
    #也可以用下面的形式来设置
    # radio_button.setChecked(not radio_button.isChecked())

push_button.clicked.connect(cao)        #点击切换另外两个按钮的切换状态


#设置按钮不可以被点击
# push_button.setEnabled(False)
# radio_button.setEnabled(False)
# checkbox_button.setEnabled(False)



#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())