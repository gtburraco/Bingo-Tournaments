from abc import ABC, abstractmethod
from typing import List


class BaseCard(ABC):
    """
    Abstract base class for all types of Bingo cards.
    """

    def __init__(self, card_id: int, numbers_grid: List[int], invalid: bool = False):
        # Validation for card_id (must be integer > 0)
        if not isinstance(card_id, int) or card_id <= 0:
            raise ValueError("Card_id must be a positive integer")

        if not isinstance(numbers_grid, list):
            raise TypeError("Numbers_grid must be a list")

        self.card_id: int = card_id
        self.numbers_grid: List[int] = numbers_grid
        self.invalid: bool = invalid
        self._mset = set(self.numbers_grid)
        self._sum = sum(self.numbers_grid)

    def to_dict(self):
        """Returns a dictionary representation of the card."""
        return {
            "type": self.__class__.__name__,
            "card_id": self.card_id,
            "numbers_grid": self.numbers_grid,
            "invalid": self.invalid,
        }

    @classmethod
    def from_dict(cls, data):
        target_type_name = data.get("type")

        for subclass in cls.__subclasses__():
            if subclass.__name__ == target_type_name:
                return subclass(
                    card_id=data["card_id"],
                    numbers_grid=data["numbers_grid"],
                    invalid=data.get("invalid", False)
                )
        raise ValueError(f"Unknown card type: {target_type_name}")

    def numbers_not_in_sequence_equal_to(self, other_card: BaseCard) -> bool:
        if self._sum != other_card._sum:
            return False
        return self._mset == other_card._mset

    def numbers_in_sequence_equal_to(self, other_card: BaseCard) -> bool:
        if self._sum != other_card._sum:
            return False
        return self.numbers_grid == other_card.numbers_grid

    @abstractmethod
    def to_html(self) -> str:
        pass
