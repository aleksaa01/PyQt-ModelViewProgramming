from utils import AppWindow

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QAbstractListModel, Qt, QModelIndex
from PyQt5.QtGui import QPixmap, QIcon, QColor

import sys


class LanguagesListModel(QAbstractListModel):
    """
    # Custom model for ListView
    # required methods: rowCount, data
    # requied methods for making model editable: flags, setData
    """

    def __init__(self, languages=None, parent=None):
        super().__init__(parent)
        self._languages = languages if languages else []

    def rowCount(self, parent=QModelIndex()):
        return len(self._languages)

    def data(self, index, role):
        if role == Qt.EditRole:
            return self._languages[index.row()]

        if role == Qt.ToolTipRole:
            return 'Programming language: ' + str(self._languages[index.row()])

        if role == Qt.DisplayRole:
            return self._languages[index.row()]

        if role == Qt.DecorationRole:
            row = index.row()
            pixmap = QPixmap(26, 26)
            hex_color = '#'
            for offset in range(6):
                hex_color += str((row + offset * row) % 10)
            pixmap.fill(QColor(hex_color))

            icon = QIcon(pixmap)
            return icon

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            row = index.row()
            self._languages[row] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def insertRows(self, position, rows, parent=QModelIndex()):
        # Methods: beginInsertRows() and endInsertRows()
        # They emit a signal that notifies the views,
        # so that views can respond corectly.
        self.beginInsertRows(parent, position, position + rows - 1)

        for i in range(rows):
            self._languages.insert(position, 'Generic language ' + str(rows - i))

        self.endInsertRows()
        return True

    def removeRows(self, position, rows, parent=QModelIndex()):
        # Methods: beginRemoveRows() and endRemoveRows()
        # They emit a signal that notifies the views,
        # so that views can respond corectly.
        self.beginRemoveRows(parent, position, position + rows - 1)

        for i in range(rows):
            del self._languages[position]

        self.endRemoveRows()
        return True

    def addData(self, new_data):
        self._languages = new_data

    def checkData(self):
        if self._languages:
            return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    language_model = LanguagesListModel()

    app_window = AppWindow(model=language_model)
    app_window.add_test_widgets()
    app_window.insertModelRows(4, 5)
    app_window.show()
    app_window.removeModelRows(4, 4)

    sys.exit(app.exec_())