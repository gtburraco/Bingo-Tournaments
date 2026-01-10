from PySide6.QtWidgets import QDialog, QHeaderView

from UI.viewUICard_ui import Ui_ViewUICard
from global_var import GV
from shared import highlight_numbers, add_number_to_cell


class ViewBoard(QDialog, Ui_ViewUICard):
    def __init__(self, parent, size_x: int, size_y: int, rows: int, cols: int):
        super().__init__(parent)
        self.setupUi(self)
        self.main_window = parent
        self.setWindowTitle(self.tr("Bingo Board"))
        self.resize(size_x, size_y)

        num = 1
        self.CardWidget.setRowCount(rows)
        self.CardWidget.setColumnCount(cols)

        for r in range(rows):
            for c in range(cols):
                add_number_to_cell(self.CardWidget, r, c, num)
                num += 1

        self.CardWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.CardWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def check_cards(self):
        highlight_numbers(self.CardWidget, GV.tournament_extracted_numbers)

    def closeEvent(self, event):
        if self.main_window and self in self.main_window.card_non_modal_windows:
            self.main_window.card_non_modal_windows.remove(self)
        super().closeEvent(event)
