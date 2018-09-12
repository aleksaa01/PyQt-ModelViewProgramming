from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QListView, QComboBox
from PyQt5.QtCore import QStringListModel


class AppWindow():

    def __init__(self, model=None, parent=None):
        # Get a window and set up required properties
        self.window = QMainWindow(parent)
        self.central_widget = QWidget()
        # You can set layout only on central widget of the main window
        self.window.setCentralWidget(self.central_widget)
        self.window.setFixedSize(640, 480)

        # Setting a model, if model is custom, add default data
        # but only if there is no data in that model
        dummy_data = ['Python', 'C++', 'Javascript', 'C#', 'Swift']
        if model is None:
            # if model is None, assume and create QStringListModel
            self._model = QStringListModel(dummy_data)
        else:
            self._model = model
            try:
                if not self._model.checkData():
                    self._model.addData(dummy_data)
            except AttributeError:
                raise Exception('Add method "checkData" that checks if data is present in your model, '
                                'and method "addData" that adds data to your model.')

        # create layout and apply it to central widget
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

    def addWidget(self, widget, set_model=False):
        self.layout.addWidget(widget)
        if set_model:
            widget.setModel(self._model)

    def insertModelRows(self, position, rows):
        num_rows = self._model.rowCount(None)
        if position <= num_rows:
            self._model.insertRows(position, rows)
        else:
            raise IndexError('Index out of range.\n'
                             'Number of rows is {}, '
                             'position supplied is {}'.format(num_rows, position))

    def removeModelRows(self, position, rows):
        num_rows = self._model.rowCount(None)
        if position <= num_rows and position + rows <= num_rows:
            self._model.removeRows(position, rows)
        else:
            raise IndexError('Index out of range.\n'
                             'Rows to delete: {}\n'
                             'Total number of rows: {}\n'
                             'Starting row: {}'.format(rows, num_rows, position))

    def insertModelColumns(self, position, columns):
        num_columns = self._model.columnCount(None)
        if position <= num_columns:
            self._model.insertColumns(position, columns)
        else:
            raise IndexError('Index out of range.\n'
                             'Number of columns is {}, '
                             'position supplied is {}'.format(num_columns, position))

    def removeModelColumns(self, position, columns):
        num_columns = self._model.columnCount(None)
        if position <= num_columns and position + columns <= num_columns:
            self._model.removeColumns(position, columns)
        else:
            raise IndexError('Index out of range.\n'
                             'Columns to delete: {}\n'
                             'Total number of columns: {}\n'
                             'Starting column: {}'.format(columns, num_columns, position))
