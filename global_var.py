import os
import random
from typing import List
from enum import Enum
import json

from Classes import BaseCard


class TournamentType(Enum):
    NONE = 0
    BINGO_60_20 = 6020
    BINGO_75_24 = 7524
    BINGO_75_25 = 7525
    BINGO_90_15 = 9015
    BINGO_100_25 = 10025

class GV:
    tournament_path = None
    tournament_type: TournamentType = TournamentType.NONE
    tournament_max_number: int = 0
    tournament_extracted_numbers: List[int] = []
    tournament_number_in_card: int = 0
    tournament_cards = [] #BaseCard

    @classmethod
    def reset(cls):
        cls.tournament_path = None
        cls.tournament_type = TournamentType.NONE
        cls.tournament_max_number = 0
        cls.tournament_extracted_numbers = []
        cls.tournament_number_in_card = 0
        cls.tournament_cards = []

    @classmethod
    def draw_number(cls)-> int:
        if len(cls.tournament_extracted_numbers)==cls.tournament_max_number:
            return 0

        while True:
            num = random.randint(1, cls.tournament_max_number)
            if num not in GV.tournament_extracted_numbers:
                return num


    @classmethod
    def save_to_json(cls):
        try:
            with open(cls.tournament_path, "w", encoding="utf-8") as f:
                json.dump(cls.to_dict(), f, indent=4)
            print(f"Data successfully saved to {cls.tournament_path}")
            return True
        except Exception as e:
            print(f"Error saving data: {e}")
            return False

    @classmethod
    def load_from_json(cls, filepath):

        if not os.path.exists(filepath):
            print("No save file found.")
            return False

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            cls.tournament_type = TournamentType[data.get("tournament_type")]
            cls.tournament_max_number = data.get("tournament_max_number")
            cls.tournament_extracted_numbers = data.get("tournament_extracted_numbers", [])
            cls.tournament_number_in_card = data.get("tournament_number_in_card")

            # Reconstruct Card objects from the raw dictionary data

            raw_cards = data.get("tournament_cards", [])
            cls.tournament_cards = [BaseCard.from_dict(c) for c in raw_cards]

            print("Data successfully loaded.")
            return True
        except Exception as e:
            print(f"Error loading data: {e}")
            raise e

    @classmethod
    def to_dict(cls):
         return {
            "tournament_type": cls.tournament_type.name,  # Save as string (e.g., "BINGO_75_24")
            "tournament_max_number": cls.tournament_max_number,
            "tournament_extracted_numbers": cls.tournament_extracted_numbers,
            "tournament_number_in_card": cls.tournament_number_in_card,
            "tournament_cards": [card.to_dict() for card in cls.tournament_cards]
        }

