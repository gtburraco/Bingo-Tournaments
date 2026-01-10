from typing import List

from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtGui import QBrush, QColor, QPainter, QPen, QFont
from PySide6.QtWidgets import QStyledItemDelegate, QStyleOptionViewItem

from global_var import GV


class CardsTableModel(QAbstractTableModel):
    HIGHLIGHT_COLOR = QColor("#FFF59D")
    BINGO_COLOR = QColor("#FFFFFF")

    def __init__(self, cards: List[BaseCard], parent=None):
        super().__init__(parent)
        self._cards: List[BaseCard] = cards

    def set_cards(self, cards: List[BaseCard]):
        self.beginResetModel()
        self._cards = cards
        self.endResetModel()

    def rowCount(self, parent=QModelIndex()):
        return len(self._cards)

    def columnCount(self, parent=QModelIndex()):
        return GV.tournament_number_in_card + 1  # colonna 0 = ID

    def data(self, index: QModelIndex, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.BackgroundRole and not GV.tournament_extracted_numbers:
            return QBrush(Qt.BrushStyle.NoBrush)

        card = self._cards[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            if index.column() == 0:
                return sum(1 for n in card.numbers_grid if n in GV.tournament_extracted_numbers)
            return card.numbers_grid[index.column() - 1]

        if role == Qt.ItemDataRole.FontRole and index.column() == 0:
            font = QFont()
            font.setItalic(True)
            return font

        if role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignCenter

        if role == Qt.ItemDataRole.UserRole:
            return card

        if role == Qt.ItemDataRole.BackgroundRole and index.column() > 0:
            num = card.numbers_grid[index.column() - 1]
            if num in GV.tournament_extracted_numbers:
                return QBrush(self.HIGHLIGHT_COLOR)
            return QBrush(Qt.BrushStyle.NoBrush)

        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = Qt.ItemDataRole.DisplayRole):
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        if orientation == Qt.Orientation.Horizontal:
            return "Drawn" if section == 0 else f"N{section}"

        if orientation == Qt.Orientation.Vertical:
            return str(self._cards[section].card_id) if self._cards else None

        return None

    def clear_backgrounds(self):
        if not self._cards:
            return
        top_left = self.index(0, 0)
        bottom_right = self.index(self.rowCount() - 1, self.columnCount() - 1)
        self.dataChanged.emit(top_left, bottom_right, [Qt.ItemDataRole.BackgroundRole, Qt.ItemDataRole.DisplayRole])

    def find_row_by_id(self, search_id: int) -> int:
        # Supponiamo che il Model memorizzi una lista di oggetti 'Sostituzione'
        for row, card in enumerate(self._cards):
            if card.card_id == search_id:
                return row
        return -1

    def notify_number_extracted(self, number: int):
        indexes_to_update = []
        for row, card in enumerate(self._cards):
            if number in card.numbers_grid:
                col = card.numbers_grid.index(number) + 1  # colonna 0 = DRAW
                index = self.index(row, col)
                indexes_to_update.append(index)
                break  # one number per card

        for index in indexes_to_update:
            self.dataChanged.emit(index, index, [Qt.ItemDataRole.BackgroundRole])


class StrikeThroughDelegate(QStyledItemDelegate):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keyword = "1"
        self.red_pen = QPen(QColor("red"), 1)

    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        user_value: BaseCard = None
        user_value = index.model().index(index.row(), 0).data(Qt.ItemDataRole.UserRole)
        if user_value.invalid:
            painter.save()
            painter.setPen(self.red_pen)
            y = option.rect.center().y()
            painter.drawLine(option.rect.left(), y, option.rect.right(), y)
            painter.restore()


class FirstColumnDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option: QStyleOptionViewItem, index):
        super().paint(painter, option, index)

        # Draw a thicker right border only for the first column (index 0)
        if index.column() == 0:
            painter.save()  # Save painter state to avoid affecting other cells

            pen = QPen(Qt.GlobalColor.black)
            width = 3  # Set the desired thickness
            pen.setWidth(width)
            # Use FlatCap to avoid the line protruding beyond the cell height
            pen.setCapStyle(Qt.PenCapStyle.FlatCap)

            painter.setPen(pen)
            rect = option.rect

            # Optimization: offset the X position by half the width
            # to ensure the line is perfectly aligned with the edge
            x_pos = rect.right() - (width // 2)

            painter.drawLine(x_pos, rect.top(), x_pos, rect.bottom())

            painter.restore()  # Restore original painter state
