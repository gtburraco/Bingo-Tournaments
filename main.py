import csv
import os
import sys
import platform
from random import randint
from typing import Optional
from PySide6.QtCore import Qt, QStandardPaths, QSize, QEvent
from PySide6.QtGui import QCloseEvent, QPalette, QColor, QFont, QIcon, QIntValidator, QKeyEvent
from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QDialog, \
    QHeaderView, QLabel, QListWidgetItem
from PySide6 import QtSvg, QtSvgWidgets


import generate
from Classes import CardsTableModel
from Classes.BaseCardModel import FirstColumnDelegate, StrikeThroughDelegate
from UI.main_window_ui import Ui_MainWindow
from generate_choice import GenerateChoice
from global_var import GV, TournamentType
from manual_draw import ManualDraw
from new_tournament import NewTournament
from print import Print
from shared import show_error, show_info, show_warning, show_question
from view_100_25 import View100_25
from view_30_09 import View30_09
from view_60_20 import View60_20
from view_75_24 import View75_24
from view_75_25 import View75_25
from view_80_16 import View80_16
from view_90_15 import View90_15
from view_board import ViewBoard


class MainWindow(QMainWindow, Ui_MainWindow):
    card_non_modal_windows: list[QDialog]

    def __init__(self):
        super().__init__()
        self.card_non_modal_windows = []

        self.setupUi(self)
        self.setWindowTitle(QApplication.applicationName() + " - " + QApplication.applicationVersion())
        if platform.system() == "Darwin":
            print("MacOS")
            ext = ".icns"
        else:
            print("Windows")
            ext = ".ico"
	
        self.setWindowIcon(QIcon(resource_path(f"Icons/ico/Icon{ext}")))
        self.AutomaticDraw.clicked.connect(self.automatic_draw)
        self.UndoDraw.clicked.connect(self.undo_draw)
        self.ManualDraw.clicked.connect(self.manual_draw)
        self.ShowBoard.clicked.connect(self.show_board)

        self.ActionNewT.triggered.connect(self.open_new_tournament_dialog)
        self.ActionNewT.setIconVisibleInMenu(True)
        self.ActionNewT.setIcon(QIcon(resource_path("Icons/svg/file_new.svg")))

        self.ActionLoadT.triggered.connect(self.load_tournament_dialog)
        self.ActionLoadT.setIconVisibleInMenu(True)
        self.ActionLoadT.setIcon(QIcon(resource_path("Icons/svg/file_open.svg")))


        self.ActionGenerate.triggered.connect(self.generate)
        self.ActionGenerate.setIconVisibleInMenu(True)
        self.ActionGenerate.setIcon(QIcon(resource_path("Icons/svg/generate.svg")))

        self.ActionDeleteExtracetd.triggered.connect(self.delete_extracted)
        self.ActionDeleteExtracetd.setIconVisibleInMenu(True)
        self.ActionDeleteExtracetd.setIcon(QIcon(resource_path("Icons/svg/delete_history.svg")))

        self.ActionExportCSV.triggered.connect(self.export_to_csv)
        self.ActionExportCSV.setIconVisibleInMenu(True)
        self.ActionExportCSV.setIcon(QIcon(resource_path("Icons/svg/csv.svg")))

        self.ActionExportHtml.triggered.connect(self.print)
        self.ActionExportHtml.setIconVisibleInMenu(True)
        self.ActionExportHtml.setIcon(QIcon(resource_path("Icons/svg/print.svg")))

        self.ActionAbout.triggered.connect(self.show_info)
        self.ActionAbout.setIconVisibleInMenu(True)
        self.ActionAbout.setIcon(QIcon(resource_path("Icons/svg/info.svg")))

        self.ActionExit.triggered.connect(self.close)
        self.ActionExit.setIconVisibleInMenu(True)
        self.ActionExit.setIcon(QIcon(resource_path("Icons/svg/exit.svg")))

        self.ViewCardToolButton.clicked.connect(self.tool_show_card)
        self.ViewCardToolButton.setIcon(QIcon(resource_path("Icons/svg/preview.svg")))

        self.InvalidateCardToolButton.clicked.connect(self.tool_invalidate_card)
        self.InvalidateCardToolButton.setIcon(QIcon(resource_path("Icons/svg/invalidate.svg")))

        self.SearchCardToolButton.clicked.connect(self.search_card)
        self.SearchCardToolButton.setIcon(QIcon(resource_path("Icons/svg/search.svg")))

        self.modelCard = CardsTableModel(GV.tournament_cards, self)

        self.TableCardsView.setModel(self.modelCard)
        self.TableCardsView.verticalHeader().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
        self.TableCardsView.installEventFilter(self)
        self.TableCardsView.doubleClicked.connect(self.cards_double_click)
        delegateFC = FirstColumnDelegate()
        delegateST = StrikeThroughDelegate()
        self.TableCardsView.setItemDelegateForColumn(0, delegateFC)
        self.TableCardsView.setItemDelegate(delegateST)

        self.status_cards_number = QLabel("")
        self.status_cards_number.setToolTip(self.tr("Total number of bingo cards in the game."))
        self.status_file_name = QLabel("")
        self.status_file_name.setToolTip(self.tr("File name of the tournament."))
        self.status_number_draw = QLabel("")
        self.status_number_draw.setToolTip(self.tr("Number of drawn numbers."))

        self.statusBar().addWidget(self.status_cards_number, 0)
        self.statusBar().addWidget(self.status_number_draw, 0)
        self.statusBar().addWidget(self.status_file_name, 1)

        self.SearchCards.setValidator(QIntValidator(0, 9999999, self))
        self.SearchCards.returnPressed.connect(self.search_card)

    # TableCardsView FILTER
    def eventFilter(self, source, event):
        if source != self.TableCardsView:
            return super().eventFilter(source, event)

        if event.type() == QEvent.Type.FocusOut:
            self.TableCardsView.clearSelection()

        if event.type() == event.Type.KeyPress and isinstance(event, QKeyEvent):
            if  Qt.Key.Key_0 <= event.key() <= Qt.Key.Key_9:
                self.SearchCards.setText(event.text())
                self.SearchCards.setFocus()

        return super().eventFilter(source, event)

    def search_card(self):
        if not self.SearchCards.text():
            return
        row = self.modelCard.find_row_by_id(int(self.SearchCards.text()))
        self.SearchCards.clear()
        if row < 0:
            return
        self.TableCardsView.selectRow(row)
        self.TableCardsView.setFocus()

    def tool_show_card(self):
        if not GV.tournament_cards:
            return

        rows = self.TableCardsView.selectionModel().selectedRows()

        for index in rows:
            row = index.row()
            card = index.data(Qt.ItemDataRole.UserRole)
            self.show_non_modal_card(card)

    def tool_invalidate_card(self):
        if not GV.tournament_cards:
            return

        rows = self.TableCardsView.selectionModel().selectedRows()

        for index in rows:
            card = index.data(Qt.ItemDataRole.UserRole)
            card.invalid = not card.invalid

        self.TableCardsView.viewport().update()
        GV.save_to_json()

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

        if GV.tournament_max_number == 30:
            dialog = ViewBoard(self, 600, 200, 3, 10)

        if GV.tournament_max_number == 60:
            dialog = ViewBoard(self, 600, 200, 6, 10)

        if GV.tournament_max_number == 75:
            dialog = ViewBoard(self, 600, 200, 5, 15)

        if GV.tournament_max_number == 80:
            dialog = ViewBoard(self, 600, 320, 8, 10)

        if GV.tournament_max_number == 90:
            dialog = ViewBoard(self, 600, 360, 9, 10)

        if GV.tournament_max_number == 100:
            dialog = ViewBoard(self, 600, 400, 10, 10)

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

        if GV.tournament_type == TournamentType.BINGO_30_09:
            dialog = View30_09(self, card)

        if GV.tournament_type == TournamentType.BINGO_60_20:
            dialog = View60_20(self, card)

        if GV.tournament_type == TournamentType.BINGO_75_24:
            dialog = View75_24(self, card)

        if GV.tournament_type == TournamentType.BINGO_75_25:
            dialog = View75_25(self, card)

        if GV.tournament_type == TournamentType.BINGO_80_16:
            dialog = View80_16(self, card)

        if GV.tournament_type == TournamentType.BINGO_90_15:
            dialog = View90_15(self, card)

        if GV.tournament_type == TournamentType.BINGO_100_25:
            dialog = View100_25(self, card)

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
        QApplication.processEvents()
        try:
            value, no_same_position, no_different_position = dialog.get_data()
            generated = generate.generate_tournament_cards(value, no_same_position, no_different_position)
        finally:
            QApplication.restoreOverrideCursor()
        if generated:
            show_info(self, self.tr("Generated {ncards} cards".format(ncards=generated)))
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
            show_error(self, e, self.tr("Error load tournament."))
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

        print(f"Broadcast to  {len(self.card_non_modal_windows)} windows")

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

        print(f"Undo Draw called {num}")

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

        print(f"Draw called {num}")

    def manual_draw(self):
        if not GV.tournament_cards:
            return
        dialog = ManualDraw(self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
        num = dialog.get_data()
        if num <= 0 or num > GV.tournament_max_number:
            show_warning(self, self.tr("Number between 1 and {numb}").format(numb=GV.tournament_max_number))
            return
        if num in GV.tournament_extracted_numbers:
            show_warning(self, self.tr("Number {numb} already draw.").format(numb=num))
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
                header = ['ID'] + ['Invalid'] + [f'N{i + 1}' for i in range(GV.tournament_number_in_card)]
                writer.writerow(header)

                for card in GV.tournament_cards:
                    row = [card.card_id] + [card.invalid] + card.numbers_grid
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
        show_info(self, QApplication.applicationVersion() + "\nBy GTBurraco")


### [ MAIN ] ##################################################################
def resource_path(relative_path) -> str:
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    return str(os.path.join(base_path, relative_path))


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Bingo Tournaments")
    app.setApplicationVersion("2.4")
	
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(240, 240, 240))
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, Qt.white)
    palette.setColor(QPalette.AlternateBase, QColor(233, 231, 227))
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.black)
    palette.setColor(QPalette.Text, Qt.black)
    palette.setColor(QPalette.Button, QColor(240, 240, 240))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    # 🔹 Close splash di PyInstaller
    if hasattr(sys, "_MEIPASS"):
        try:
            import pyi_splash
            pyi_splash.close()
        except ImportError:
            pass
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
