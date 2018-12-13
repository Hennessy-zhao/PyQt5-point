from PyQt5.Qt import *

#print(QObject.__subclasses__())  #输出所有的子类

#print(QWidget.__subclasses__())  #输出所有的子类

#print(QAbstractButton.__subclasses__())  #输出所有的子类




def getSubClass(cls):
    for subClass in cls.__subclasses__():
        print(subClass)
        if len(subClass.__subclasses__())>0:
            getSubClass(subClass)


getSubClass(QAbstractButton)