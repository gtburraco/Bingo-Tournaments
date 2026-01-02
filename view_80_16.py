from UI.viewUICard_ui import Ui_ViewUICard
from PySide6.QtWidgets import QDialog, QHeaderView
from Classes.card80_16 import Card80_16
from global_var import GV
from shared import highlight_numbers, add_number_to_cell

class View80_16(QDialog, Ui_ViewUICard):
    def __init__(self, parent, card: Card80_16):
        super().__init__(parent)
        self.setupUi(self)
        self.main_window = parent
        self.setWindowTitle(str(card.card_id))

        self.resize(300, 300)
        self.CardWidget.setRowCount(4)
        self.CardWidget.setColumnCount(4)


        positions = [
            [(0, 0), (0, 1), (0, 2), (0, 3)],  # r 1
            [(1, 0), (1, 1), (1, 2), (1, 3)],  # r 2
            [(2, 0), (2, 1), (2, 2), (2, 3)],  # r 3
            [(3, 0), (3, 1), (3, 2), (3, 3)],  # r 4
        ]
        idx = 0
        for row in positions:
            for r, c in row:
                add_number_to_cell(self.CardWidget, r, c, card.numbers_grid[idx])
                idx += 1

        self.CardWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.CardWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def check_cards(self):
        highlight_numbers(self.CardWidget,GV.tournament_extracted_numbers)

    def closeEvent(self, event):
        if self.main_window and self in self.main_window.card_non_modal_windows:
            self.main_window.card_non_modal_windows.remove(self)
        super().closeEvent(event)

