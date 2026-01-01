from typing import List

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QFontMetrics
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout, QMessageBox


def highlight_numbers(table, numbers_to_highlight) -> List[int]:
    numbers_highlighted: List[int] = []
    for r in range(table.rowCount()):
        for c in range(table.columnCount()):
            cell_widget = table.cellWidget(r, c)
            if cell_widget is not None:
                label = cell_widget.layout().itemAt(0).widget()
                if label.text() != "" and int(label.text()) in numbers_to_highlight:
                    label.setStyleSheet("background-color: #FFF59D;")
                    numbers_highlighted.append(int(label.text()))
                else:
                    label.setStyleSheet("background-color: none;")
    return  numbers_highlighted


def add_number_to_cell(table, row, col, number):
    padding_h = 2
    padding_v = 2
    label = QLabel(str(number))
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(padding_h,padding_v,padding_h,padding_v) # left, top, right, bottom
    #layout.setContentsMargins(6, 4, 6, 4)
    layout.addWidget(label)

    table.setCellWidget(row, col, container)

    def resize_font(event):
        w = container.width() - (2*padding_h)
        h = container.height() - (2*padding_v)
        if w == 0 or h == 0:
            return
        font = QFont()
        font_size = 1
        while True:
            font.setPointSize(font_size)
            metrics = QFontMetrics(font)
            if metrics.horizontalAdvance(str(number)) > w or metrics.height() > h:
                font.setPointSize(max(1, font_size - 1))
                break
            font_size += 1
        label.setFont(font)

    container.resizeEvent = resize_font
    resize_font(None)


def show_error(parent: QWidget, e: Exception, text: str):
    msg = QMessageBox(
        QMessageBox.Icon.Critical,
        parent.tr("Error"),
        text,
        QMessageBox.StandardButton.Ok,
        parent
    )
    if e is not None:
        msg.setDetailedText(str(e))
    msg.exec()


def show_warning(parent: QWidget, text: str, details: str = None):
    msg = QMessageBox(
        QMessageBox.Icon.Warning,
        parent.tr("Warning"),
        text,
        QMessageBox.StandardButton.Ok,
        parent
    )
    if details:
        msg.setDetailedText(details)
    msg.exec()



def show_info(parent: QWidget, text: str, details: str = None):
    msg = QMessageBox(
        QMessageBox.Icon.Information,
        parent.tr("Information"),
        text,
        QMessageBox.StandardButton.Ok,
        parent
    )
    if details:
        msg.setDetailedText(details)
    msg.exec()

def show_question(parent: QWidget, text: str, details: str = None) -> bool:
    return QMessageBox.question(parent, parent.tr("Question"), text,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No) == QMessageBox.StandardButton.Yes
