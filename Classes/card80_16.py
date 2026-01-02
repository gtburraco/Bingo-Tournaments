from typing import List
from .base_card import BaseCard

class Card80_16(BaseCard):
    def __init__(self, card_id: int, numbers_grid: List[int]):
        # Call the constructor of the parent class (BaseCard)
        super().__init__(card_id, numbers_grid)

    def to_html(self) -> str:
        st = '<td width="25%">'
        et = '</td>\n'
        tr = '</tr><tr>\n'

        html = "<table>\n<tbody>\n"
        html += f"<tr><td colspan='4'><b>{self.card_id}</b></td>"+tr

        html += ''.join(st + str(n) + et for n in self.numbers_grid[0:4]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[4:8]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[8:12]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[12:16]) + tr

        html += '<td colspan="4" align="center" valign="middle" style="font-size: xx-small;">Bingo Software&copy; - By GTBurraco</td></tr>\n'
        html += "</tbody></table>\n"
        return html

