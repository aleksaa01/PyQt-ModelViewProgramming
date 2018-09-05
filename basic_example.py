from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, \
    QListView, QComboBox
from PyQt5.QtCore import QStringListModel

import sys


class AppWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.setFixedSize(640, 480)

        data = ['one', 'two', 'three', 'four', 'five']
        model = QStringListModel(data)

        layout = QVBoxLayout()

        listview = QListView()
        combobox = QComboBox()
        listview2 = QListView()
        combobox2 = QComboBox()

        listview.setModel(model)
        combobox.setModel(model)
        listview2.setModel(model)
        combobox2.setModel(model)

        layout.addWidget(listview)
        layout.addWidget(combobox)
        layout.addWidget(listview2)
        layout.addWidget(combobox2)

        central_widget.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    app_window = AppWindow()
    app_window.show()
    sys.exit(app.exec_())
