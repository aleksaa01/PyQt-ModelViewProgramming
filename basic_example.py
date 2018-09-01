from utils import AppWindow

from PyQt5 import QtWidgets, QtCore
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app_window = AppWindow()
    app_window.add_test_widgets()
    app_window.show()
    sys.exit(app.exec_())
