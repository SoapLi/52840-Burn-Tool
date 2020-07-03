import sys

from PyQt5 import QtWidgets

from LJHCpuidMenu import LJHToolMainMenu


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    testShow = LJHToolMainMenu()
    testShow.show()
    sys.exit(app.exec_())
