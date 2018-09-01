from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QListView, QComboBox
from PyQt5.QtCore import QStringListModel


class AppWindow():

    def __init__(self, data=None, model=None, parent=None):
        # Get a window and set up required properties
        self.window = QMainWindow(parent)
        self.central_widget = QWidget()
        # You can set layout only on central widget of the main window
        self.window.setCentralWidget(self.central_widget)
        self.window.setFixedSize(640, 480)

        # Setting data required by model
        if data is None:
            self._data = ['Python', 'C++', 'Javascript', 'C#', 'Swift']
        else:
            self._data = data

        # Setting a model, if model is custom, add default data
        # but only if there is no data in that model
        if model is None:
            self._model = QStringListModel(self._data)
        else:
            self._model = model
            if not self._model.checkData():
                self._model.addData(self._data)

        # initialize layout and apply it to central widget
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

    def add_test_widgets(self):
        # Add basic widgets for testing the model.

        listview = QListView()
        combobox = QComboBox()
        listview2 = QListView()
        combobox2 = QComboBox()

        listview.setModel(self._model)
        combobox.setModel(self._model)
        listview2.setModel(self._model)
        combobox2.setModel(self._model)

        self.layout.addWidget(listview)
        self.layout.addWidget(combobox)
        self.layout.addWidget(listview2)
        self.layout.addWidget(combobox2)

    def show(self):
        self.window.show()

    def addWidget(self, widget):
        self.layout.addWidget(widget)
