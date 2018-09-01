from utils import AppWindow

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtGui import QPixmap, QIcon, QColor

import sys


class LanguagesListModel(QAbstractListModel):
    # Custom model for ListView
    # required methods: rowCount, data

    def __init__(self, languages=None, parent=None):
        super().__init__(parent)
        self._languages = languages if languages else []

    def rowCount(self, parent):
        return len(self._languages)

    def data(self, index, role):
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
    app_window.show()

    sys.exit(app.exec_())