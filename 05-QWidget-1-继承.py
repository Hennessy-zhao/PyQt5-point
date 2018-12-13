from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)

print(QWidget.__bases__)        #打印QWidget继承的类，直接继承
print(QWidget.mro())            #检索链条，查看QWidget往上的继承链


sys.exit(app.exec_())