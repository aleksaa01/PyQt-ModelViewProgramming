from utils import AppWindow

from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QAbstractListModel, Qt
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
        if role == Qt.DisplayRole:
            return 'Display data'

    def addData(self, new_data):
        self._languages = new_data

    def checkData(self):
        if self._languages:
            return True
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    new_model = LanguagesListModel()

    app_window = AppWindow(model=new_model)
    app_window.add_test_widgets()
    app_window.show()

    sys.exit(app.exec_())