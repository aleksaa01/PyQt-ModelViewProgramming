from PyQt5 import QtWidgets, QtCore
import sys

class AppWindow():

    def __init__(self, parent=None):
        self.window = QtWidgets.QMainWindow(parent)
        self.central_widget = QtWidgets.QWidget()
        self.window.setCentralWidget(self.central_widget)
        self.window.setFixedSize(640, 480)

        layout = QtWidgets.QVBoxLayout()

        data = ['one', 'two', 'three', 'four', 'five']

        listview = QtWidgets.QListView()
        combobox = QtWidgets.QComboBox()
        listview2 = QtWidgets.QListView()
        combobox2 = QtWidgets.QComboBox()

        model = QtCore.QStringListModel(data)
        listview.setModel(model)
        combobox.setModel(model)
        listview2.setModel(model)
        combobox2.setModel(model)

        layout.addWidget(listview)
        layout.addWidget(combobox)
        layout.addWidget(listview2)
        layout.addWidget(combobox2)

        self.central_widget.setLayout(layout)

    def show(self):
        self.window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec_())
