# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("综合案例")
        self.resize(500,500)

        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }

        self.setup_ui()

    def setup_ui(self):
        # 1.创建两个下拉列表控件
        pro=QComboBox(self)
        city=QComboBox(self)
        pro.move(100,100)
        city.move(200,100)

        self.pro=pro
        self.city=city



        # 3.监听省的下拉列表的当前值发生改变的信号
        pro.currentIndexChanged[str].connect(self.pro_changed)
        #self.pro_changed(pro.currentText())

        # 3.监听城市的下拉列表的当前值发生改变的信号
        city.currentIndexChanged[int].connect(self.city_changed)
        #self.city_changed(city.currentIndex())

        # 2.展示数据到第一个下拉选择控件当中
        pro.addItems(self.city_dic.keys())


    def pro_changed(self,pro_name):
        # print(pro_name)
        # 1.根据省的名称，到字典里面，获取对应的城市字典
        citys=self.city_dic[pro_name]
        # print(citys)
        self.city.blockSignals(True)
        self.city.clear()                       #此时阻断了信号，防止了因为清空而触发信号
        self.city.blockSignals(False)
        #self.city.addItems(citys.keys())
        for key, val in citys.items():
            self.city.addItem(key, val)


    def city_changed(self,city_index):
        # print(city_index)
        print(self.city.itemData(city_index))

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())