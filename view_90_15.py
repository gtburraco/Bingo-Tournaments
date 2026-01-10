from PySide6.QtWidgets import QDialog, QHeaderView

from Classes.card90_15 import Card90_15
from UI.viewUICard_ui import Ui_ViewUICard
from global_var import GV
from shared import highlight_numbers, add_number_to_cell


class View90_15(QDialog, Ui_ViewUICard):
    def __init__(self, parent, card: Card90_15):
        super().__init__(parent)
        self.setupUi(self)
        self.main_window = parent
        self.setWindowTitle(str(card.card_id))

        self.resize(500, 200)
        self.CardWidget.setRowCount(3)
        self.CardWidget.setColumnCount(9)

        col_ranges = [
            (1, 9), (10, 19), (20, 29), (30, 39), (40, 49),
            (50, 59), (60, 69), (70, 79), (80, 90)
        ]

        # Popolamento della tabella
        for r in range(3):
            row_numbers = card.numbers_grid[r * 5:(r + 1) * 5]  # i 5 numeri della riga
            for c, (fr, to) in enumerate(col_ranges):
                number_to_show = card.get_pos_in_range(fr, to, row_numbers)
                add_number_to_cell(self.CardWidget, r, c, number_to_show)

        self.CardWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.CardWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def check_cards(self):
        highlight_numbers(self.CardWidget, GV.tournament_extracted_numbers)

    def closeEvent(self, event):
        if self.main_window and self in self.main_window.card_non_modal_windows:
            self.main_window.card_non_modal_windows.remove(self)
        super().closeEvent(event)
