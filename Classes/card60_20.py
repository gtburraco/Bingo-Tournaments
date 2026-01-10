from typing import List

from .base_card import BaseCard


class Card60_20(BaseCard):
    def __init__(self, card_id: int, numbers_grid: List[int], invalid: bool = False):
        # Call the constructor of the parent class (BaseCard)
        super().__init__(card_id, numbers_grid, invalid)

    def to_html(self) -> str:
        st = '<td width="20%">'
        et = '</td>\n'
        tr = '</tr><tr>\n'

        html = "<table>\n<tbody>\n"
        html += f"<tr><td colspan='5'><b>{self.card_id}</b></td>" + tr

        html += ''.join(st + str(n) + et for n in self.numbers_grid[0:5]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[5:10]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[10:15]) + tr
        html += ''.join(st + str(n) + et for n in self.numbers_grid[15:20]) + tr

        html += '<td colspan="5" align="center" valign="middle" style="font-size: xx-small;">Bingo Software&copy; - By GTBurraco</td></tr>\n'
        html += "</tbody></table>\n"
        return html
