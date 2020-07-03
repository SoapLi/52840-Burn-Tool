from PyQt5.QtCore import pyqtSignal


class GlobalData:
    signal1 = 0

    def __init__(self):
        super(GlobalData, self).__init__()

    def get_signal1(self):
        return self.signal1

    def set_signal1(self):
        self.signal1 = pyqtSignal()