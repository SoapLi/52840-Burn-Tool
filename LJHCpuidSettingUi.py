

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 295)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 141, 221))
        self.groupBox.setObjectName("groupBox")
        self.pushButtonCleanChipList = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonCleanChipList.setGeometry(QtCore.QRect(10, 30, 121, 23))
        self.pushButtonCleanChipList.setObjectName("pushButtonCleanChipList")
        self.pushButtonExit = QtWidgets.QPushButton(Form)
        self.pushButtonExit.setGeometry(QtCore.QRect(560, 260, 75, 23))
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 20, 471, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_LoadHex = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_LoadHex.setGeometry(QtCore.QRect(390, 70, 71, 23))
        self.pushButton_LoadHex.setObjectName("pushButton_LoadHex")
        self.lineEdit_LoadHex = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_LoadHex.setGeometry(QtCore.QRect(10, 40, 451, 21))
        self.lineEdit_LoadHex.setObjectName("lineEdit_LoadHex")
        self.pushButton_Merge = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_Merge.setGeometry(QtCore.QRect(180, 180, 75, 23))
        self.pushButton_Merge.setObjectName("pushButton_Merge")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 131, 16))
        self.label.setObjectName("label")
        self.lineEdit_LoadSoftDeviceHex = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_LoadSoftDeviceHex.setGeometry(QtCore.QRect(10, 100, 451, 21))
        self.lineEdit_LoadSoftDeviceHex.setObjectName("lineEdit_LoadSoftDeviceHex")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 221, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_LoadSoftDeviceHex = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_LoadSoftDeviceHex.setGeometry(QtCore.QRect(390, 130, 71, 23))
        self.pushButton_LoadSoftDeviceHex.setObjectName("pushButton_LoadSoftDeviceHex")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Config"))
        self.pushButtonCleanChipList.setText(_translate("Form", "Clean Chip Id List"))
        self.pushButtonExit.setText(_translate("Form", "EXIT"))
        self.groupBox_2.setTitle(_translate("Form", "Merge Tool"))
        self.pushButton_LoadHex.setText(_translate("Form", "Load"))
        self.pushButton_Merge.setText(_translate("Form", "Merge It"))
        self.label.setText(_translate("Form", "Load nrf52840_xxaa.hex"))
        self.label_2.setText(_translate("Form", "Load s140_nrf52_6.1.1_softdevice.hex"))
        self.pushButton_LoadSoftDeviceHex.setText(_translate("Form", "Load"))


