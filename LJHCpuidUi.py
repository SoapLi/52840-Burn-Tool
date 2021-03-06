
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(628, 409)
        self.pushButtonStartBurn = QtWidgets.QPushButton(Dialog)
        self.pushButtonStartBurn.setGeometry(QtCore.QRect(440, 300, 171, 41))
        self.pushButtonStartBurn.setObjectName("pushButtonStartBurn")
        self.textEditLog = QtWidgets.QTextEdit(Dialog)
        self.textEditLog.setGeometry(QtCore.QRect(20, 40, 391, 271))
        self.textEditLog.setObjectName("textEditLog")
        self.labelImgPath = QtWidgets.QLabel(Dialog)
        self.labelImgPath.setGeometry(QtCore.QRect(80, 360, 541, 21))
        self.labelImgPath.setText("")
        self.labelImgPath.setObjectName("labelImgPath")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 360, 61, 16))
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(500, 10, 111, 41))
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setObjectName("lcdNumber")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(450, 20, 41, 20))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(430, 60, 191, 291))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_About = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_About.setGeometry(QtCore.QRect(30, 140, 131, 31))
        self.pushButton_About.setObjectName("pushButton_About")
        self.pushButtonWorkPath = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonWorkPath.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.pushButtonWorkPath.setObjectName("pushButtonWorkPath")
        self.pushButtonCpuList = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCpuList.setGeometry(QtCore.QRect(30, 60, 131, 31))
        self.pushButtonCpuList.setObjectName("pushButtonCpuList")
        self.pushButtonSetting = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonSetting.setGeometry(QtCore.QRect(30, 22, 131, 31))
        self.pushButtonSetting.setObjectName("pushButtonSetting")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(30, 180, 131, 51))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBoxModeSelect = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBoxModeSelect.setGeometry(QtCore.QRect(20, 20, 101, 21))
        self.comboBoxModeSelect.setObjectName("comboBoxModeSelect")
        self.comboBoxModeSelect.addItem("")
        self.comboBoxModeSelect.addItem("")
        self.groupBox_3.raise_()
        self.pushButton_About.raise_()
        self.pushButtonWorkPath.raise_()
        self.pushButtonCpuList.raise_()
        self.pushButtonSetting.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 20, 411, 331))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButtonCleanLog = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButtonCleanLog.setGeometry(QtCore.QRect(350, 300, 51, 20))
        self.pushButtonCleanLog.setObjectName("pushButtonCleanLog")
        self.pushButtonSelectImg = QtWidgets.QPushButton(Dialog)
        self.pushButtonSelectImg.setGeometry(QtCore.QRect(10, 380, 81, 23))
        self.pushButtonSelectImg.setObjectName("pushButtonSelectImg")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.pushButtonStartBurn.raise_()
        self.textEditLog.raise_()
        self.labelImgPath.raise_()
        self.label_2.raise_()
        self.lcdNumber.raise_()
        self.label.raise_()
        self.pushButtonSelectImg.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonStartBurn.setText(_translate("Dialog", "Start"))
        self.label_2.setText(_translate("Dialog", "hex path :"))
        self.label.setText(_translate("Dialog", "Index："))
        self.pushButton_About.setText(_translate("Dialog", "About"))
        self.pushButtonWorkPath.setText(_translate("Dialog", "Work Path"))
        self.pushButtonCpuList.setText(_translate("Dialog", "Chip ID List"))
        self.pushButtonSetting.setText(_translate("Dialog", "Setting"))
        self.groupBox_3.setTitle(_translate("Dialog", "Mode"))
        self.comboBoxModeSelect.setItemText(0, _translate("Dialog", "BURN"))
        self.comboBoxModeSelect.setItemText(1, _translate("Dialog", "CPU ID"))
        self.groupBox_2.setTitle(_translate("Dialog", "Log:"))
        self.pushButtonCleanLog.setText(_translate("Dialog", "Clean"))
        self.pushButtonSelectImg.setText(_translate("Dialog", "choose..."))


