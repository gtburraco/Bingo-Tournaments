import csv
import sys
from random import randint
from typing import Optional

from PySide6.QtCore import Qt, QStandardPaths, QSize, QEvent
from PySide6.QtGui import QCloseEvent, QColor, QFont
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QDialog, \
    QHeaderView, QLabel, QListWidgetItem

import generate
from Classes import CardsTableModel
from Classes.BaseCardModel import FirstColumnDelegate
from UI.main_window_ui import Ui_MainWindow
from generate_choice import GenerateChoice
from global_var import GV, TournamentType
from manual_draw import ManualDraw
from new_tournament import NewTournament
from print import Print
from shared import show_error, show_info, show_warning, show_question
from view_100_25 import View100_25
from view_75_24 import View75_24
from view_75_25 import View75_25
from view_board import ViewBoard
from view_90_15 import View90_15

class MainWindow(QMainWindow, Ui_MainWindow):
    card_non_modal_windows: list[QDialog]

    def __init__(self):
        super().__init__()

        self.card_non_modal_windows = []

        self.setupUi(self)

        self.AutomaticDraw.clicked.connect(self.automatic_draw)
        self.UndoDraw.clicked.connect(self.undo_draw)
        self.ManualDraw.clicked.connect(self.manual_draw)
        self.ShowBoard.clicked.connect(self.show_board)

        self.ActionNewT.triggered.connect(self.open_new_tournament_dialog)
        self.ActionLoadT.triggered.connect(self.load_tournament_dialog)
        self.ActionGenerate.triggered.connect(self.generate)
        self.ActionDeleteExtracetd.triggered.connect(self.delete_extracted)
        self.ActionExportCSV.triggered.connect(self.export_to_csv)
        self.ActionExportHtml.triggered.connect(self.print)
        self.ActionAbout.triggered.connect(self.show_info)
        self.ActionExit.triggered.connect(self.close)

        self.ViewCardToolButton.clicked.connect(self.tool_show_card)

        self.modelCard = CardsTableModel(GV.tournament_cards, self)

        self.TableCardsView.setModel(self.modelCard)
        self.TableCardsView.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableCardsView.installEventFilter(self)
        self.TableCardsView.doubleClicked.connect(self.cards_double_click)
        delegate = FirstColumnDelegate()
        self.TableCardsView.setItemDelegateForColumn(0, delegate)
        self.status_cards_number = QLabel("")
        self.status_file_name = QLabel("")
        self.status_number_draw = QLabel("")

        self.statusBar().addWidget(self.status_cards_number, 0)
        self.statusBar().addWidget(self.status_number_draw, 0)
        self.statusBar().addWidget(self.status_file_name, 1)

    # TableCardsView FILTER
    def eventFilter(self, source, event):
        if source == self.TableCardsView and event.type() == QEvent.Type.FocusOut:
            self.TableCardsView.clearSelection()
        return super().eventFilter(source, event)

    def tool_show_card(self):
        if not GV.tournament_cards:
            return

        rows = self.TableCardsView.selectionModel().selectedRows()

        for index in rows:
            row = index.row()
            card = index.data(Qt.ItemDataRole.UserRole)
            self.show_non_modal_card(card)


    def cards_double_click(self):
        if not GV.tournament_cards:
            return

        selection = self.TableCardsView.selectionModel().currentIndex()

        if not selection:
            return

        self.show_non_modal_card(selection.data(Qt.ItemDataRole.UserRole))

    def show_board(self):
        if not GV.tournament_cards:
            return

        for dlg in self.card_non_modal_windows:
            if dlg.property("card_id") == 0:
                dlg.raise_()
                return

        dialog: Optional[QDialog] = None

        if GV.tournament_max_number == 75:
            dialog = ViewBoard(self,600,200,5,15)

        if GV.tournament_max_number == 100:
            dialog = ViewBoard(self, 600, 400, 10, 10)

        if GV.tournament_max_number == 90:
            dialog = ViewBoard(self, 600, 360, 9, 10)

        if not dialog:
            return

        dialog.setProperty("card_id", 0)
        dialog.show()
        dialog.check_cards()
        self.card_non_modal_windows.append(dialog)

    def show_non_modal_card(self, card):

        for dlg in self.card_non_modal_windows:
            if dlg.property("card_id") == card.card_id:
                dlg.raise_()
                return

        dialog: Optional[QDialog] = None

        if GV.tournament_type == TournamentType.BINGO_75_24:
            dialog = View75_24(self, card)

        if GV.tournament_type == TournamentType.BINGO_75_25:
            dialog = View75_25(self, card)

        if GV.tournament_type == TournamentType.BINGO_100_25:
            dialog = View100_25(self, card)

        if GV.tournament_type == TournamentType.BINGO_90_15:
            dialog = View90_15(self, card)

        if not dialog:
            return

        dialog.setProperty("card_id", card.card_id)
        dialog.show()
        dialog.move(dialog.x() + randint(-80, 80), dialog.y() + randint(-80, 80))

        dialog.check_cards()
        self.card_non_modal_windows.append(dialog)

    def generate(self):
        if GV.tournament_type == TournamentType.NONE:
            return

        if GV.tournament_extracted_numbers:
            show_warning(self, self.tr("Cards cannot be generated if the numbers have already been drawn."))
            return

        dialog = GenerateChoice(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        try:
            generate.generate_tournament_cards(dialog.get_data())
        finally:
            QApplication.restoreOverrideCursor()

        self.update_and_save()
        print(f"Total cards in tournament: {len(GV.tournament_cards)}")

    def update_and_save(self):
        self.status_cards_number.setText(str(len(GV.tournament_cards)))
        self.update_cards_table()
        self.update_lcd()
        GV.save_to_json()

    def load_tournament_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            self.tr("Open Tournament File"),
            QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation),
            "Bingo Tournament (*.bt);;All Files (*.*)")

        if not file_path:
            return

        QApplication.setOverrideCursor(Qt.CursorShape.WaitCursor)
        try:
            GV.load_from_json(file_path)
            GV.tournament_path = file_path
            self.modelCard.set_cards(GV.tournament_cards)
            self.update_cards_table()
            self.update_and_save()
            self.status_file_name.setText(GV.tournament_path)

            for num in GV.tournament_extracted_numbers:
                self.add_extracted_ball(num)

            self.ActionLoadT.setEnabled(False)
            self.ActionNewT.setEnabled(False)

        except Exception as e:
            show_error(self, e, "Error load tournament.")
        finally:
            QApplication.restoreOverrideCursor()

    def update_lcd(self):
        if GV.tournament_extracted_numbers:
            self.LcdNumber.display(GV.tournament_extracted_numbers[-1])
        else:
            self.LcdNumber.display("")

    def open_new_tournament_dialog(self):
        dialog = NewTournament(self)

        if dialog.exec() != QDialog.DialogCode.Accepted:
            return

        self.status_file_name.setText(GV.tournament_path)

        GV.save_to_json()
        show_info(self, self.tr("Tournament created.\nNow generate cards"))
        self.ActionLoadT.setEnabled(False)
        self.ActionNewT.setEnabled(False)
        self.update_cards_table()

    def closeEvent(self, event: QCloseEvent):
        if show_question(self, self.tr("Are you sure you want to quit?")):
            event.accept()
        else:
            event.ignore()

    def update_cards_table(self):
        # if not GV.tournament_cards:
        #    self.TableCardsView.setModel(None)
        #    return

        self.TableCardsView.setUpdatesEnabled(False)
        self.TableCardsView.setModel(CardsTableModel(GV.tournament_cards))
        self.TableCardsView.resizeColumnsToContents()
        self.TableCardsView.resizeRowToContents(0)
        row_height = self.TableCardsView.rowHeight(0)
        self.TableCardsView.verticalHeader().setDefaultSectionSize(row_height)
        self.TableCardsView.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Fixed)
        self.TableCardsView.setUpdatesEnabled(True)

    ### [ CONTROL MODAL ] ##################################################################
    def broadcast_highlight(self):
        # print(f"broadcast to windows ",len(self.card_non_modal_windows))
        for window in self.card_non_modal_windows:
            window.check_cards()

    ### [ DRAW ] ##################################################################
    def delete_extracted(self):
        if not GV.tournament_extracted_numbers:
            return
        GV.tournament_extracted_numbers.clear()

        self.modelCard.clear_backgrounds()
        self.TableCardsView.viewport().update()

        self.remove_all_ball()
        self.drow_update()
        self.broadcast_highlight()

    def undo_draw(self):
        if not GV.tournament_extracted_numbers:
            return

        num = GV.tournament_extracted_numbers[-1]
        del GV.tournament_extracted_numbers[-1]

        self.modelCard.notify_number_extracted(num)
        self.TableCardsView.viewport().update()

        self.remove_last_ball()
        self.drow_update()
        self.broadcast_highlight()

    def automatic_draw(self, manual_number=None):
        if not GV.tournament_cards:
            return

        num = manual_number or GV.draw_number()
        if num == 0:
            return

        GV.tournament_extracted_numbers.append(num)
        self.add_extracted_ball(num)
        self.drow_update()

        self.modelCard.notify_number_extracted(num)
        self.TableCardsView.viewport().update()
        self.broadcast_highlight()
        if manual_number:
            self.manual_draw()

        # print("Automatic draw called", num)
        # print(GV.tournament_cards[0])

    def manual_draw(self):
        if not GV.tournament_cards:
            return
        dialog = ManualDraw(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        num = dialog.get_data()
        if num <= 0 or num > GV.tournament_max_number:
            show_warning(self, self.tr("Number between 1 and %d" % GV.tournament_max_number))
            return
        if num in GV.tournament_extracted_numbers:
            show_warning(self, self.tr("Number %d already draw." % num))
            return
        self.automatic_draw(num)

    def drow_update(self):
        self.status_number_draw.setText(str(len(GV.tournament_extracted_numbers)))
        self.update_lcd()
        GV.save_to_json()

    ### [ BALL ] ##################################################################
    def remove_last_ball(self):
        item = self.ListNumberDraw.takeItem(self.ListNumberDraw.count() - 1)
        del item
        self.ListNumberDraw.scrollToBottom()

    def remove_all_ball(self):
        self.ListNumberDraw.clear()
        self.ListNumberDraw.scrollToTop()

    def add_extracted_ball(self, number):
        item = QListWidgetItem(str(number))
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        item.setFont(font)
        item.setSizeHint(QSize(30, 30))
        item.setBackground(QColor("#FFD700"))
        self.ListNumberDraw.addItem(item)
        self.ListNumberDraw.scrollToBottom()

    ### [ EXPORT ] ##################################################################
    def export_to_csv(self):
        if not GV.tournament_cards:
            return

        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Export to csv"),
            QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation),
            "Bingo Cards (*.csv);;All Files (*.*)"
        )
        if not file_path:
            return
        if not file_path.lower().endswith(".csv"):
            file_path += ".csv"

        try:
            with open(file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter=';')
                header = ['ID'] + [f'N{i + 1}' for i in range(GV.tournament_number_in_card)]
                writer.writerow(header)

                # 3. Scrivi i dati delle cartelle
                for card in GV.tournament_cards:
                    row = [card.card_id] + card.numbers_grid
                    writer.writerow(row)

            show_info(self, self.tr("Export completed!"))

        except Exception as e:
            show_error(self, e, self.tr("Export Error"))

    ### [ PRINT ] ##################################################################
    def print(self):
        if not GV.tournament_cards:
            return
        dialog = Print()
        dialog.exec()

    ### [ INFO ] ##################################################################
    def show_info(self):
        show_info(self, "Version 2.0")


### [ MAIN ] ##################################################################

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
