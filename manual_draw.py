from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog

from UI.manual_draw_ui import Ui_ManualDraw
from shared import show_warning


class ManualDraw(QDialog, Ui_ManualDraw):
    _last_position = None
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._value: int = 0

        if ManualDraw._last_position:
            self.move(ManualDraw._last_position)

        self.buttonBox.accepted.connect(self.validate_and_accept)
        self.buttonBox.rejected.connect(self.reject)

    def validate_and_accept(self):
        raw_text = self.lineEdit.text().strip()
        try:
            self._value = int(raw_text)
            ManualDraw._last_position = self.pos()
            self.accept()

        except ValueError:
            show_warning(self, self.tr("Insert a number."))

    def get_data(self) -> int:
        return self._value

    def closeEvent(self, event):
        ManualDraw._last_position = self.pos()
        super().closeEvent(event)