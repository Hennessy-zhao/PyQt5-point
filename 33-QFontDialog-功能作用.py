# -*- coding:UTF-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog")
        self.resize(500,500)
        self.setup_ui()

    def setup_ui(self):
        # fd = QFontDialog(self)
        font=QFont()
        font.setFamily("宋体")
        font.setPointSize(30)
        fd=QFontDialog(font)
        fd.setCurrentFont(font)     #修改当前字体
        # fd.setOption(QFontDialog.NoButtons)             #不显示“ 确定”和“ 取消”按钮。
        fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)             #不显示“ 确定”和“ 取消”按钮。

        print(fd.testOption(QFontDialog.MonospacedFonts))           #检查QFontDialog.MonospacedFonts是否生效

        btn=QPushButton(self)
        btn.setText("按钮")
        btn.move(100,100)


        def font_sel():
            print("字体已经被选择",fd.selectedFont().family())

        btn.clicked.connect(lambda :fd.open(font_sel))
        # if fd.exec_():
        #     print(fd.selectedFont().family())

        label=QLabel(self)
        label.move(200,100)
        label.setText("Hennessy")

        def cfc(font):
            label.setFont(font)
            label.adjustSize()
        fd.currentFontChanged.connect(cfc)





if __name__=='__main__':
    app=QApplication(sys.argv)
    form=Demo()
    form.show()
    sys.exit(app.exec_())