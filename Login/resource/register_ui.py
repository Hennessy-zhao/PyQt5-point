# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 450)
        Form.setMinimumSize(QtCore.QSize(500, 450))
        Form.setMaximumSize(QtCore.QSize(500, 450))
        Form.setStyleSheet("QWidget#Form{\n"
"    border-image: url(:/register/images/register_background.jpg);\n"
"}")
        self.main_menu_btn = QtWidgets.QPushButton(Form)
        self.main_menu_btn.setGeometry(QtCore.QRect(10, 20, 50, 50))
        self.main_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253, 167, 255);\n"
"    color:white;\n"
"    border:2px solid rgb(250, 218, 218);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.main_menu_btn.setCheckable(True)
        self.main_menu_btn.setObjectName("main_menu_btn")
        self.about_menu_btn = QtWidgets.QPushButton(Form)
        self.about_menu_btn.setGeometry(QtCore.QRect(90, 0, 50, 50))
        self.about_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253, 167, 255);\n"
"    color:white;\n"
"    border:2px solid rgb(250, 218, 218);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.about_menu_btn.setCheckable(False)
        self.about_menu_btn.setObjectName("about_menu_btn")
        self.reset_menu_btn = QtWidgets.QPushButton(Form)
        self.reset_menu_btn.setGeometry(QtCore.QRect(70, 70, 50, 50))
        self.reset_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253, 167, 255);\n"
"    color:white;\n"
"    border:2px solid rgb(250, 218, 218);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.reset_menu_btn.setCheckable(False)
        self.reset_menu_btn.setObjectName("reset_menu_btn")
        self.exit_menu_btn = QtWidgets.QPushButton(Form)
        self.exit_menu_btn.setGeometry(QtCore.QRect(0, 90, 50, 50))
        self.exit_menu_btn.setStyleSheet("QPushButton{\n"
"    border-radius:25px;\n"
"    background-color:rgb(253, 167, 255);\n"
"    color:white;\n"
"    border:2px solid rgb(250, 218, 218);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    border:4px double rgb(239, 160, 179);\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"    background-color:rgb(209, 0, 209);\n"
"}")
        self.exit_menu_btn.setCheckable(False)
        self.exit_menu_btn.setObjectName("exit_menu_btn")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 180, 251, 212))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("color:rgb(204,204,204);\n"
"font: 12pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.account_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.account_le.setMinimumSize(QtCore.QSize(0, 35))
        self.account_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(240, 240, 240);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;")
        self.account_le.setClearButtonEnabled(True)
        self.account_le.setObjectName("account_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.account_le)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("color:rgb(204,204,204);\n"
"font: 12pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_le.setMinimumSize(QtCore.QSize(0, 35))
        self.password_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(240, 240, 240);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;")
        self.password_le.setClearButtonEnabled(True)
        self.password_le.setObjectName("password_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_le)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setStyleSheet("color:rgb(204,204,204);\n"
"font: 12pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.confirm_pwd_le = QtWidgets.QLineEdit(self.layoutWidget)
        self.confirm_pwd_le.setMinimumSize(QtCore.QSize(0, 35))
        self.confirm_pwd_le.setStyleSheet("background-color:transparent;\n"
"color:rgb(240, 240, 240);\n"
"border:none;\n"
"border-bottom:1px solid lightgrey;")
        self.confirm_pwd_le.setClearButtonEnabled(True)
        self.confirm_pwd_le.setObjectName("confirm_pwd_le")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_pwd_le)
        self.register_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.register_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.register_btn.sizePolicy().hasHeightForWidth())
        self.register_btn.setSizePolicy(sizePolicy)
        self.register_btn.setMinimumSize(QtCore.QSize(0, 45))
        self.register_btn.setStyleSheet("QPushButton{    \n"
"    background-color: rgb(255, 170, 127);\n"
"    color:rgb(201,0,94);\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"QPushButton:hover{    \n"
"    background-color: rgb(255, 192, 167);\n"
"}\n"
"QPushButton:pressed{    \n"
"    background-color: rgb(218, 145, 108);\n"
"}\n"
"\n"
"QPushButton:disabled{    \n"
"    background-color: rgb(197,197 ,197 );\n"
"}\n"
"")
        self.register_btn.setObjectName("register_btn")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.register_btn)
        self.about_menu_btn.raise_()
        self.reset_menu_btn.raise_()
        self.exit_menu_btn.raise_()
        self.layoutWidget.raise_()
        self.main_menu_btn.raise_()

        self.retranslateUi(Form)
        self.main_menu_btn.clicked['bool'].connect(Form.show_hide_menu)
        self.about_menu_btn.clicked.connect(Form.about_lk)
        self.reset_menu_btn.clicked.connect(Form.reset)
        self.exit_menu_btn.clicked.connect(Form.exit_pane)
        self.register_btn.clicked.connect(Form.check_register)
        self.account_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.password_le.textChanged['QString'].connect(Form.enable_register_btn)
        self.confirm_pwd_le.textChanged['QString'].connect(Form.enable_register_btn)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.main_menu_btn.setText(_translate("Form", "菜单"))
        self.about_menu_btn.setText(_translate("Form", "关于"))
        self.reset_menu_btn.setText(_translate("Form", "重置"))
        self.exit_menu_btn.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "账      号:"))
        self.label_2.setText(_translate("Form", "密      码:"))
        self.label_3.setText(_translate("Form", "确认密码:"))
        self.register_btn.setText(_translate("Form", "注册"))

import images_rc
