from utils import AppWindow

from PyQt5.QtWidgets import QApplication, QTableWidget, QTableView
from PyQt5.QtCore import Qt, QAbstractTableModel
from PyQt5.QtGui import QPixmap, QIcon, QColor

import sys
import random


class LanguagesTableModel(QAbstractTableModel):

    HEXADECIMAL = '0123456789abcdef'

    def __init__(self, languages=None, parent=None):
        super().__init__(parent)
        self._languages = languages if languages else [[]]

    def rowCount(self, parent):
        return len(self._languages)

    def columnCount(self, parent):
        return len(self._languages[0])

    def flags(self, index):
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def data(self, index, role):
        if role == Qt.EditRole:
            return self._languages[index.row()][index.column()]

        if role == Qt.ToolTipRole:
            return 'Programming language: ' + str(self._languages[index.row()][index.column()])

        if role == Qt.DisplayRole:
            return self._languages[index.row()][index.column()]

        if role == Qt.DecorationRole:
            row = index.row()
            column = index.column()
            pixmap = QPixmap(26, 26)
            hex_color = '#'
            for offset in range(6):
                # Creation of some enough random color, that will be the same every time.
                random.seed((row + 16) * (column + 16) + offset)
                hex_color += random.choice(self.HEXADECIMAL)
            pixmap.fill(QColor(hex_color))

            icon = QIcon(pixmap)
            return icon

    def addData(self, new_data):
        if type(new_data) != list:
            raise TypeError('new_data must be a list, got {0} instead.'.format(type(new_data)))
        for i in new_data:
            if type(i) != list:
                raise TypeError('Every item in new_data must be a list, got {0} instead.'.format(type(new_data)))
        self._languages = new_data

    def checkData(self):
        if self._languages and self._languages[0]:
            return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    language_data = [
        ['C', 'C++', 'Java', 'C#'],
        ['Python', 'Ruby', 'Haskel', 'Go'],
        ['Rust', 'Javascript', 'PHP', 'Lisp'],
        ['Perl', 'Swift', 'Kotlin', 'Objective-C']
    ]
    language_model = LanguagesTableModel(language_data)

    app_window = AppWindow(model=language_model)

    table_widget = QTableView()
    app_window.addWidget(table_widget, set_model=True)

    app_window.show()

    sys.exit(app.exec_())