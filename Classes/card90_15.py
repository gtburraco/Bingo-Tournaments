from typing import List
from .base_card import BaseCard

class Card90_15(BaseCard):
    def __init__(self, card_id: int, numbers_grid: List[int]):
        # Call the constructor of the parent class (BaseCard)
        super().__init__(card_id, numbers_grid)

    def get_pos_in_range(self, fr: int, to: int, numbers: List[int]) -> str:
        for n in numbers:
            if fr <= n <= to:
                return str(n)
        return ""

    def get_row_html(self, row_indices: List[int]) -> str:
        html = ""
        ranges = [(1, 9), (10, 19), (20, 29), (30, 39), (40, 49),
                  (50, 59), (60, 69), (70, 79), (80, 90)]
        numbers = [self.numbers_grid[i] for i in row_indices]
        for fr, to in ranges:
            html += f'<td width="11%">{self.get_pos_in_range(fr, to, numbers)}</td>\n'
        html += "</tr><tr>\n"
        return html

    def to_html(self) -> str:
        html = "<table>\n<tbody>\n"
        html += f"<tr><td colspan='9'><b>{self.card_id}</b></td></tr><tr>\n"

        html += self.get_row_html([0, 1, 2, 3, 4])
        html += self.get_row_html([5, 6, 7, 8, 9])
        html += self.get_row_html([10, 11, 12, 13, 14])

        html += '<td colspan="9" align="center" valign="middle" style="font-size: xx-small;">Bingo Software&copy; - By GTBurraco</td></tr>\n'
        html += "</tbody></table>\n"
        return html
