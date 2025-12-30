import os

from PySide6.QtCore import Qt, QStandardPaths
from PySide6.QtGui import QFontMetrics
from PySide6.QtWidgets import QDialog,  QFileDialog

from UI.new_tournament_ui import Ui_NewTournament
from global_var import GV, TournamentType
from shared import show_warning, show_error


class NewTournament(QDialog, Ui_NewTournament):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.validate_and_accept)
        self.buttonBox.rejected.connect(self.reject)
        self.FolderButton.clicked.connect(self.handle_save_file)

        self._selected_full_path = ""

    def handle_save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            self.tr("Create Tournament File"),
            QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation),
            "Bingo Tournament (*.bt);;All Files (*.*)"
        )

        self.selected_full_path = ""
        if file_path:
            if not file_path.lower().endswith(".bt"):
                file_path += ".bt"
            self.FolderChoice.setText(self.elide_path(file_path))
            self._selected_full_path = file_path

    def elide_path(self, path: str) -> str:
        metrics = QFontMetrics(self.FolderChoice.font())
        width = self.FolderChoice.width() - 10
        return metrics.elidedText(path, Qt.TextElideMode.ElideLeft, width)

    def validate_and_accept(self):
        if not self._selected_full_path:
            show_warning(self,self.tr("Please select a destination file for the tournament."))
            return

        folder_path = os.path.dirname(self._selected_full_path)
        if not os.path.exists(folder_path):
            show_warning(self,self.tr("The directory where you want to save the file does not exist."))
            return

        GV.tournament_path = self._selected_full_path

        if self.RadioButton75_24.isChecked():
            GV.tournament_type = TournamentType.BINGO_75_24
            GV.tournament_max_number = 75
            GV.tournament_number_in_card = 24
        if self.RadioButton75_25.isChecked():
            GV.tournament_type = TournamentType.BINGO_75_25
            GV.tournament_max_number = 75
            GV.tournament_number_in_card = 25
        if self.RadioButton90_15.isChecked():
            GV.tournament_type = TournamentType.BINGO_90_15
            GV.tournament_max_number = 90
            GV.tournament_number_in_card = 15
        if self.RadioButton100_25.isChecked():
            GV.tournament_type = TournamentType.BINGO_100_25
            GV.tournament_max_number = 100
            GV.tournament_number_in_card = 25

        self.accept()
