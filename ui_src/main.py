# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\wolf\PycharmProjects\pfc_demo\ui_src\main.ui',
# licensing of 'C:\Users\wolf\PycharmProjects\pfc_demo\ui_src\main.ui' applies.
#
# Created: Mon Dec 23 14:58:34 2019
#      by: pyside2-uic  running on PySide2 5.11.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 634)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.status_name = QtWidgets.QLineEdit(Form)
        self.status_name.setObjectName("status_name")
        self.horizontalLayout_2.addWidget(self.status_name)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.auto_name = QtWidgets.QLineEdit(Form)
        self.auto_name.setObjectName("auto_name")
        self.horizontalLayout_3.addWidget(self.auto_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.forward_number = QtWidgets.QLineEdit(Form)
        self.forward_number.setObjectName("forward_number")
        self.horizontalLayout.addWidget(self.forward_number)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL("clicked()"), Form.make_sample)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL("clicked()"), Form.clear)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL("clicked()"), Form.save)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL("clicked()"), Form.parallel_bond)
        QtCore.QObject.connect(self.pushButton_5, QtCore.SIGNAL("clicked()"), Form.ucs)
        QtCore.QObject.connect(self.pushButton_6, QtCore.SIGNAL("clicked()"), Form.plot_stress_strain)
        QtCore.QObject.connect(self.pushButton_9, QtCore.SIGNAL("clicked()"), Form.cycle)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "保存状态：", None, -1))
        self.status_name.setPlaceholderText(QtWidgets.QApplication.translate("Form", "保存状态名", None, -1))
        self.pushButton_3.setText(QtWidgets.QApplication.translate("Form", "保存", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate("Form", "清空工作区", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "生成试样", None, -1))
        self.pushButton_4.setText(QtWidgets.QApplication.translate("Form", "生成parallel bond连接", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("Form", "自动保存文件名", None, -1))
        self.auto_name.setText(QtWidgets.QApplication.translate("Form", "ucs_{{index}}", None, -1))
        self.pushButton_5.setText(QtWidgets.QApplication.translate("Form", "单轴压缩", None, -1))
        self.pushButton_6.setText(QtWidgets.QApplication.translate("Form", "应力位移曲线", None, -1))
        self.forward_number.setPlaceholderText(QtWidgets.QApplication.translate("Form", "前进的帧数", None, -1))
        self.pushButton_9.setText(QtWidgets.QApplication.translate("Form", "前进", None, -1))

