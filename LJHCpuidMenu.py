import os
import sys
import json
import threading as thd
import time
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtCore import QFileInfo, QUrl, QCoreApplication
from PyQt5.QtGui import QTextCursor, QDesktopServices, QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from LJHCpuidUi import Ui_Dialog
from LJHCpuidSettingMenu import LJHToolSettingMenu


class LJHToolMainMenu(QtWidgets.QWidget, Ui_Dialog):
    # userGuideInfo = "此软件用于烧录nrf52840 camera 固件！\n" \
    #                 "使用前请阅读《产品装配测试说明》并安装所需环境(Command-Line-Tools_10_5_0_Installer_64.exe 与 python-3.7.4-amd64.exe)\n" \
    #                 + "\n" \
    #                 + "注意事项：\n" \
    #                 + "1.行如果发现卡死，请检查硬件是否连接正常然后重启软件再试\n" \
    #                 + "2.请勿修改或删除安装目录下load_hex_file_without_eraseuicr.bat 脚本\n"
    userGuideInfo = "This software is used for burning  nrf52840！\n" \
                    "Please install (Command-Line-Tools_10_5_0_Installer_64.exe and  python-3.7.4-amd64.exe) first\n" \
                    + "\n" \
                    + "Warning：\n" \
                    + "1.do not remove/modify  load_hex_file_without_eraseuicr.bat and merge_hex2.bat\n"
    version = "V1.4"
    burnImgPath = ''
    cpuid0_addr = 10000060
    cpuid1_addr = 10000064
    total_number = "Total_number"
    current_cpuid = os.getcwd() + '\\cpuid.log'
    cpuidlist = os.getcwd() + '\\cpuidlist.txt'
    hexFileForBurn = os.getcwd() + '\\nrf52840_withsoftdevice.hex'
    bat_revalue = 99
    num = 0
    cpuid = ''
    color_red = "#ff0000"
    color_green = "#00ff00"
    color_black = "#000000"
    wait_cnt = 0
    widget_setting = 0

    def __init__(self):
        super(LJHToolMainMenu, self).__init__()
        self.widget_setting = LJHToolSettingMenu()
        self.setupUi(self)

        self.setWindowTitle("XXX Tool " + self.version)
        self.setWindowIcon(QIcon(os.getcwd() + '\\logo.ico'))
        self.pushButtonStartBurn.clicked.connect(self.click_start_test)
        self.pushButtonWorkPath.clicked.connect(self.click_open_work_path)
        self.pushButtonSetting.clicked.connect(self.click_select_setting)
        self.textEditLog.textChanged.connect(self.slot_update_ui)
        self.pushButtonCpuList.clicked.connect(self.click_open_cpu_list)
        self.pushButton_About.clicked.connect(self.click_open_about_info)
        self.pushButtonSelectImg.clicked.connect(self.click_select_img)
        self.pushButtonCleanLog.clicked.connect(self.click_clean_log)
        self.comboBoxModeSelect.currentIndexChanged.connect(self.slot_mode_select)
        self.widget_setting.signal_setting_ok.connect(self.slot_update_setting)
        self.widget_setting.signal_merge_ok.connect(self.slot_update_hex_file)
        self.check_chipidlist()
        self.slot_update_ui()

    def check_chipidlist(self):
        if not os.path.exists(self.cpuidlist):
            with open("%s" % self.cpuidlist, "a", encoding="utf-8") as file_w:
                file_w.write(" {\"Total_number\": 0}")
                file_w.close()

    def check_img_name(self):
        special_str = "~!@#$%^&*()+-*<>,[]（）"
        for i in special_str:
            if i in self.burnImgPath:
                self.log_show("固件路径包含特殊字符：" + i, self.color_red)
                return False
        return True

    def log_show(self, log, color):
        self.textEditLog.append("<font color=\"" + color + "\">" + str(
            time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime())) + " -> " + log + "</font> ")

    def burn_sta_check_task(self):
        self.slot_update_setting()
        if 0 == self.bat_revalue:
            self.bat_revalue = 99
            self.wait_cnt = 0
            MagniCameraToolMainMenu.set_total_number_to_txt(self, self.num + 1)
            MagniCameraToolMainMenu.save_cpuid_to_cpulist(self, self.cpuid, (self.num + 1))
            print("LOGCAT: SUCCESS!!!!" + str(self.cpuid))
            self.log_show("BURN SUCCESS!!!!", self.color_green)
            self.pushButtonStartBurn.setText('Start')
            self.pushButtonStartBurn.setEnabled(1)
            return
        if 1 == self.bat_revalue:
            self.bat_revalue = 99
            self.wait_cnt = 0
            print("LOGCAT: ERR!!!!")
            self.log_show("BURN ERR!!!!", self.color_red)
            self.pushButtonStartBurn.setText('Start')
            self.pushButtonStartBurn.setEnabled(1)
            return
        if 99 == self.bat_revalue:
            print('LOGCAT: WAITE!!!!')
            self.wait_cnt = self.wait_cnt + 1
            if self.wait_cnt > 10:
                self.bat_revalue = 99
                self.wait_cnt = 0
                print("LOGCAT: DEVICE CONNECT ERR!!!!")
                self.log_show("LOGCAT: DEVICE CONNECT ERR!!!!", self.color_red)
                self.pushButtonStartBurn.setText('Start')
                self.pushButtonStartBurn.setEnabled(1)
                return
            thd.Timer(1, self.burn_sta_check_task).start()
            self.log_show("BURNING..." + str(self.wait_cnt), self.color_black)
            self.pushButtonStartBurn.setText('BURNING...')
            self.pushButtonStartBurn.setDisabled(1)

    def load_chipid_burn_to_flash(self):
        self.cpuid = self.get_serial_number_from_board()
        self.log_show("cpuid is : " + self.cpuid, self.color_black)
        self.num = self.get_total_number_of_devs()
        self.log_show("This is device : " + str(self.num + 1), self.color_black)
        self.log_show("start load_hex_file...", self.color_black)
        # self.bat_revalue = os.system('load_hex_file_without_eraseuicr.bat' + " " + self.burnImgPath)
        self.bat_revalue = subprocess.run('load_hex_file_without_eraseuicr.bat' + " " + self.burnImgPath,
                                          shell=True).returncode

    def load_chipid(self):
        self.cpuid = self.get_serial_number_from_board()
        self.log_show("cpuid is : " + self.cpuid, self.color_black)

    def get_total_number_of_devs(self):
        for line in open(self.cpuidlist, 'r').readlines():
            if self.total_number in line:
                number = json.loads(line)
                number = number[self.total_number]
                return number

    def set_total_number_to_txt(self, num):
        print('LOGCAT: Saving board number ...')
        with open(self.cpuidlist, "r", encoding="utf-8") as file_r, open("%s.bak" % self.cpuidlist, "w",
                                                                         encoding="utf-8") as file_w:
            for line in file_r.readlines():
                if self.total_number in line:
                    old_data = json.loads(line)
                    old_data[self.total_number] = num
                    new_data = json.dumps(old_data)
                    # to do :save board number to file serial_number.txt
                    line = line.replace(line, new_data)
                    file_w.write(line)
                    file_w.write('\n')
                    print("LOGCAT: " + new_data)
                else:
                    file_w.write(line)
        os.remove(self.cpuidlist)
        os.rename("%s.bak" % self.cpuidlist, self.cpuidlist)

    def save_cpuid_to_cpulist(self, id, num):
        print('LOGCAT: Saving cpuid number ...')
        with open("%s" % self.cpuidlist, "a", encoding="utf-8") as file_w:
            file_w.write(str(num))
            file_w.write(', ')
            file_w.write(id)
            file_w.write('\n')
            file_w.close()

    def get_serial_number_from_board(self):
        value = 0

        if os.path.exists(self.current_cpuid):
            print('LOGCAT: current_cpuid exists remove it' + self.current_cpuid)
            os.remove(self.current_cpuid)
        # 用nrf命令 读取cpu id0 到 current_cpuid
        # rei = os.system('nrfjprog  --memrd ' + '0x' + str(self.cpuid0_addr) + '> ' + self.current_cpuid)
        ret = subprocess.run('nrfjprog  --memrd ' + '0x' + str(self.cpuid0_addr) + '> ' + self.current_cpuid,
                             shell=True)
        if ret.returncode != 0:
            self.log_show("device not detect!", self.color_red)

        # 条件等待 current_uicr文件产生获取cpuid0_addrr
        # 解析出id部分 例如 ：0x10000060: A7D3718A
        while os.path.exists(self.current_cpuid):
            for line in open(self.current_cpuid).readlines():
                if str(self.cpuid0_addr) in line:
                    value = line[12:20]
                    # value = value[6:8] + value[4:6] + value[2:4] + value[0:2]
                    print('LOGCAT: Got cpuid0：0x' + value)
                    break;
            break;

        # 清除临时文件
        if os.path.exists(self.current_cpuid):
            os.remove(self.current_cpuid)
        # 用nrf命令 读取cpu id1 到 current_cpuid
        # os.system('nrfjprog  --memrd ' + '0x' + str(self.cpuid1_addr) + '> ' + self.current_cpuid)
        subprocess.run('nrfjprog  --memrd ' + '0x' + str(self.cpuid1_addr) + '> ' + self.current_cpuid, shell=True)

        # 条件等待 current_uicr文件产生 获取cpuid1_addr
        while os.path.exists(self.current_cpuid):
            for line in open(self.current_cpuid).readlines():
                if str(self.cpuid1_addr) in line:
                    value = line[12:20] + str(value)
                    os.remove(self.current_cpuid)
                    return value
        os.remove(self.current_cpuid)
        return 'NULL'

    def click_start_test(self):

        if self.comboBoxModeSelect.currentIndex() == 0:
            if self.burnImgPath == '':
                QMessageBox.information(self, "Warning", "please select hex file")
                return
            if not self.check_img_name():
                return
            self.textEditLog.clear()
            self.pushButtonStartBurn.setText('BURNING...')
            self.pushButtonStartBurn.setDisabled(1)
            thd.Thread(target=MagniCameraToolMainMenu.load_chipid_burn_to_flash, args=(self,)).start()
            thd.Timer(1, self.burn_sta_check_task).start()
        else:
            thd.Thread(target=MagniCameraToolMainMenu.load_chipid, args=(self,)).start()

    def click_open_work_path(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(os.getcwd()))

    def click_open_cpu_list(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self.cpuidlist))

    def click_open_about_info(self):
        QMessageBox.information(self,
                                "User Guide " + self.version,
                                self.userGuideInfo)

    def click_select_img(self):
        self.burnImgPath = QFileDialog.getOpenFileName(None, "please select hex file", './',
                                                       'ALL(*.*);;hex file(*.hex)',
                                                       'hex file(*.hex)')
        self.burnImgPath = self.burnImgPath[0]
        self.labelImgPath.setText(self.burnImgPath)

    def click_clean_log(self):
        self.textEditLog.clear()

    def click_select_setting(self):
        self.widget_setting.show()

    def slot_update_setting(self):
        self.slot_update_ui()

    def slot_mode_select(self, index):
        print(index)

    def slot_update_ui(self):
        self.lcdNumber.display(self.get_total_number_of_devs() + 1)
        self.textEditLog.moveCursor(QTextCursor.End)

    def slot_update_hex_file(self):
        self.labelImgPath.setText(self.hexFileForBurn)
        self.burnImgPath = self.hexFileForBurn
