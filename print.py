import os
import random
import webbrowser

from PySide6.QtCore import QStandardPaths

from UI.print_ui import Ui_PrintDialog
from global_var import GV
from PySide6.QtWidgets import QDialog, QFileDialog

from shared import show_error, show_info

html_head = """<!DOCTYPE html>
<head>
<style type="text/css">
body {
    margin: 0;
    padding: 0;
    font-family: Arial;
}

.page {
    display: grid;
    grid-template-columns: repeat(VAR_COLS, 1fr);
    grid-template-rows: repeat(VAR_ROWS, 1fr);
    gap: 5mm;
    page-break-after: always;
}


.card {
    border: 0px;
    padding: 2mm;
    box-sizing: border-box;
}

.card table {
    width: 100%;
    height: 100%;
    border-collapse: collapse;
}

.card td {
    border: 1px solid black;
    text-align: center;
    vertical-align: middle;
    font-size: VAR_FONT_SIZEmm;
}
table {
        border-width: 2px 2px 2px 2px;
        border-spacing: 0px;
        border-style: outset outset outset outset;
        border-color: black black black black;
        border-collapse: collapse;
    }
    table th {
        border-width: 1px 1px 1px 1px;
        padding: 1px 1px 1px 1px;
        border-style: inset inset inset inset;
        border-color: black black black black;
    }
    table td {
        border-width: 1px 1px 1px 1px;
        padding: 1px 1px 1px 1px;
        border-style: inset inset inset inset;
        border-color: black black black black;
        text-align: center;
        vertical-align: middle;
    }
</style>
</head>
<body>
"""

html_footer = """</body>"""

class Print(QDialog, Ui_PrintDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.validate_and_accept)
        self.buttonBox.rejected.connect(self.reject)

    def validate_and_accept(self):
        rows = self.Row_spinBox.value()
        cols = self.Col_spinBox.value()
        font_size = self.Font_spinBox.value()
        randomness  = self.RandomcheckBox.isChecked()
        if rows <= 0 or cols <= 0 or font_size <= 0:
            return

        file_path, selected_filter = QFileDialog.getSaveFileName(
            self,
            self.tr("Export to HTML"),
            QStandardPaths.writableLocation(QStandardPaths.StandardLocation.DocumentsLocation),
            "Bingo HTML Cards (*.html);;All Files (*.*)"
        )
        if not file_path:
            return
        if not file_path.lower().endswith(".html"):
            file_path += ".html"

        cards_per_page = cols * rows
        if cards_per_page <= 1:
            return

        html = html_head
        html = html.replace("VAR_COLS", str(cols))
        html = html.replace("VAR_ROWS", str(rows))
        html = html.replace("VAR_FONT_SIZE", str(font_size))

        #shuffled_cards = random.sample(GV.tournament_cards, len(GV.tournament_cards))
        if randomness:
            new_cards_list = random.sample(GV.tournament_cards, len(GV.tournament_cards))
        else:
            new_cards_list = GV.tournament_cards

        for i in range(0, len(new_cards_list), cards_per_page):
            html += '<div class="page">\n'
            for card in new_cards_list[i:i + cards_per_page]:
                html += '<div class="card">'+card.to_html()+'</div>\n'
            html += '</div>\n'
        html += html_footer
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(html)

        except OSError as e:
            show_error(self,e,self.tr("Error saving file"))
        else:
            show_info(self,self.tr("File saved"))
            file_url = f"file://{os.path.abspath(file_path)}"
            webbrowser.open(file_url)
            self.accept()