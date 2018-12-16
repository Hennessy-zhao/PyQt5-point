#0. 导入需要的包和模块
from PyQt5.Qt import *
import  sys

#1.创建一个应用程序对象
app=QApplication(sys.argv)


#2.控件的操作
#2.1 创建控件
window=QWidget()
#2.2 设置控件
window.setWindowTitle("QRadioButton-功能测试")
window.resize(500,500)

#当只有一个的时候，可以点击一下选中再点击一下取消。但是如果有两个及以上个单选按钮，就不能取消
rb_nan=QRadioButton("男-&Male",window)           #把Alt+M作为选中的快捷键
# rb_nan.setShortcut("Alt+M")                     #把Alt+M作为选中的快捷键
rb_nan.move(100,100)
rb_nan.setChecked(True)                 #设置为默认选中

rb_nv=QRadioButton("女-&Femaal",window)          #把Alt+F作为选中的快捷键
rb_nv.move(100,150)
rb_nv.setIcon(QIcon("./images/cusor.png"))
rb_nv.setIconSize(QSize(50,50))

rb_nv.toggled.connect(lambda isChecked: print("状态变化了，状态为：",isChecked))
# rb_nv.setAutoExclusive(False)   #设置为不是独占，则不是单选，是多选。点击一个之后，另外一个状态不会被取消

#2.3 显示控件
window.show()

#3. 应用程序执行，进入消息循环
sys.exit(app.exec_())