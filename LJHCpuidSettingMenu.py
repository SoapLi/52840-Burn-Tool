import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, pyqtSignal
from LJHCpuidSettingUi import Ui_Form
import threading as thd
import subprocess


class LJHToolSettingMenu(QtWidgets.QWidget, Ui_Form):
    cpuidlist = os.getcwd() + '\\cpuidlist.txt'
    xxaaHexPath = ''
    softDeviceHexPath = ''
    signal_setting_ok = pyqtSignal()
    signal_merge_ok = pyqtSignal()

    def __init__(self):
        super(LJHToolSettingMenu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Setting")
        self.pushButtonCleanChipList.clicked.connect(self.cleanChipIdlist)
        self.pushButtonExit.clicked.connect(self.close_menu)
        self.pushButton_LoadHex.clicked.connect(self.slot_load_hex)
        self.pushButton_LoadSoftDeviceHex.clicked.connect(self.slot_load_soft_device_hex)
        self.pushButton_Merge.clicked.connect(self.slot_merge_hex)

    def run_merge_hex2(self):
        ret = subprocess.run('merge_hex2.bat' + " " + self.softDeviceHexPath[0] + " " + self.xxaaHexPath[0], shell=True)
        if ret.returncode == 0:
            self.signal_merge_ok.emit()

    def cleanChipIdlist(self):
        ret = QMessageBox.information(self, 'Warning', 'clean cpuidlist.txt？', QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        print(ret)
        if ret == QMessageBox.Yes:
            if os.path.exists(self.cpuidlist):
                os.remove(self.cpuidlist)
                with open("%s" % self.cpuidlist, "a", encoding="utf-8") as file_w:
                    file_w.write(" {\"Total_number\": 0}")
                    file_w.close()
            self.signal_setting_ok.emit()
        else:
            pass

    def close_menu(self):
        self.close()

    def slot_load_hex(self):
        self.xxaaHexPath = QFileDialog.getOpenFileName(None, "choose ...xxaa.hex", './',
                                                       'ALL(*.*);;hex file(*.hex)',
                                                       'hex file(*.hex)')
        self.lineEdit_LoadHex.setText(self.xxaaHexPath[0])

    def slot_load_soft_device_hex(self):
        self.softDeviceHexPath = QFileDialog.getOpenFileName(None, "choose ...softdevice.hex", './',
                                                             'ALL(*.*);;hex file(*.hex)',
                                                             'hex file(*.hex)')
        self.lineEdit_LoadSoftDeviceHex.setText(self.softDeviceHexPath[0])

    def slot_merge_hex(self):
        thd.Thread(target=MagniCameraToolSettingMenu.run_merge_hex2, args=(self,)).start()
