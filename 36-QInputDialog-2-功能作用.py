# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        inputd=QInputDialog(self,Qt.FramelessWindowHint)

        # inputd.setOption(QInputDialog.UseListViewForComboBoxItems)

        inputd.setComboBoxItems(["1","2","abc"])

        inputd.setLabelText("请输入你的姓名")
        inputd.setOkButtonText("好的")
        inputd.setCancelButtonText("取消")

        # inputd.setInputMode(QInputDialog.DoubleInput)
        # inputd.setDoubleRange(9.9,19.9)
        # inputd.setDoubleStep(2)
        # inputd.setDoubleDecimals(3)

        inputd.setInputMode(QInputDialog.TextInput)
        inputd.setComboBoxItems(["abc","def","lalala"])
        inputd.setComboBoxEditable(True)

        inputd.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())