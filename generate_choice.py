from UI.generate_choice_ui import Ui_GenerateChoice
from PySide6.QtWidgets import QDialog

from shared import show_warning


class GenerateChoice(QDialog, Ui_GenerateChoice):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._value: int  = 0

        self.buttonBox.accepted.connect(self.validate_and_accept)
        self.buttonBox.rejected.connect(self.reject)
    def validate_and_accept(self):
        raw_text = self.lineEdit.text().strip()
        try:
            self._value = int(raw_text)
            self.accept()
        except ValueError:
            show_warning(self, self.tr("Insert a number."))

    def get_data(self) -> int:
        return self._value
