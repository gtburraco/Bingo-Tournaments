from abc import ABC, abstractmethod
from typing import List

class BaseCard(ABC):
    """
    Abstract base class for all types of Bingo cards.
    """
    def __init__(self, card_id: int, numbers_grid: List[int]):
        # Validation for card_id (must be integer > 0)

        self.card_id: int = card_id
        self.numbers_grid: List[int] = numbers_grid

    def to_dict(self):
        """Returns a dictionary representation of the card."""
        return {
            "type": self.__class__.__name__,
            "card_id": self.card_id,
            "numbers_grid": self.numbers_grid
        }

    @classmethod
    def from_dict(cls, data):
        target_type_name = data.get("type")

        for subclass in cls.__subclasses__():
            if subclass.__name__ == target_type_name:
                return subclass(
                    card_id=data["card_id"],
                    numbers_grid=data["numbers_grid"]
                )

        return cls(
           card_id=data.get("card_id"),
           numbers_grid=data.get("numbers_grid")
        )

    def numbers_not_in_sequence_equal_to(self, other_card: 'BaseCard') -> bool:
        set_current = set(self.numbers_grid)
        set_other = set(other_card.numbers_grid)
        return set_current == set_other

    def numbers_in_sequence_equal_to(self, other_card: 'BaseCard') -> bool:
        return self.numbers_grid == other_card.numbers_grid

    @abstractmethod
    def to_html(self) -> str:
        pass
