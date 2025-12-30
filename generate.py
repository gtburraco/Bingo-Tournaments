import random
from typing import List

from Classes.card100_25 import Card100_25
from Classes.card75_24 import Card75_24
from Classes.card75_25 import Card75_25
from Classes.card90_15 import Card90_15
from global_var import GV, TournamentType


def generate_tournament_cards(total_needed: int):
    """
    Generates the required number of cards in multiples of 3
    to maintain balanced number distribution.
    """

    all_cards = []
    max_card_id = 0

    if GV.tournament_cards:
        max_card_id = max(GV.tournament_cards, key=lambda card: card.card_id).card_id

    max_card_id += 1

    print(f"Generating {total_needed} cards, starting from {max_card_id}")

    # Loop to reach at least the total_needed (e.g., 102 for 100 required)
    if GV.tournament_type == TournamentType.BINGO_75_24:
        while len(all_cards) < total_needed:
            block = generate_3_cards_75_24(starting_id=max_card_id)
            max_card_id += 3
            all_cards.extend(block)

    if GV.tournament_type == TournamentType.BINGO_75_25:
        while len(all_cards) < total_needed:
            block = generate_3_cards_75_25(starting_id=max_card_id)
            max_card_id += 3
            all_cards.extend(block)

    if GV.tournament_type == TournamentType.BINGO_90_15:
        while len(all_cards) < total_needed:
            block = generate_6_cards_90_15(starting_id=max_card_id)
            max_card_id += 6
            all_cards.extend(block)

    if GV.tournament_type == TournamentType.BINGO_100_25:
        while len(all_cards) < total_needed:
            block = generate_4_cards_100_25(starting_id=max_card_id)
            max_card_id += 4
            all_cards.extend(block)

    GV.tournament_cards.extend(all_cards)


def get_non_existent_number(min_val: int, max_val: int, numbers_in_block: List[int]) -> int:
    """
    Finds an available number within the range that hasn't been used in the current block
    """
    # Create a list of available numbers in this specific range
    available = [n for n in range(min_val, max_val + 1) if n not in numbers_in_block]

    if not available:
        raise Exception(f"Sequence {min_val}-{max_val} is exhausted")

    # Randomly pick one from the available numbers
    chosen = random.choice(available)
    numbers_in_block.append(chosen)
    return chosen


def generate_3_cards_75_24(starting_id: int) -> List[Card75_24]:
    """
    Generates a block of 3 cards ensuring that 72 out of 75 numbers are used.
    This follows the C# logic for balanced distribution across cards.
    """
    card_objects:List[Card75_24] = []
    block_numbers: List[int] = []

    for i in range(3):
        # Initialize the 24-number list for this specific card
        card_numbers = [0] * 24

        # Mapping identical to your C# code (B:1-15, I:16-30, N:31-45, G:46-60, O:61-75)

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[1] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[2] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[3] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[4] = get_non_existent_number(61, 75, block_numbers)

        # ROW 2
        card_numbers[5] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[6] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[7] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[8] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[9] = get_non_existent_number(61, 75, block_numbers)

        # ROW 3 (Central - N column skips the center/Free Space)
        card_numbers[10] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[11] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[12] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[13] = get_non_existent_number(61, 75, block_numbers)

        # ROW 4
        card_numbers[14] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[15] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[16] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[17] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[18] = get_non_existent_number(61, 75, block_numbers)

        # ROW 5
        card_numbers[19] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[20] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[21] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[22] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[23] = get_non_existent_number(61, 75, block_numbers)

        # Instantiate the Card75_24 class with an incremented ID
        new_card = Card75_24(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    # DEBUG check: Ensure exactly 3 numbers are missing from the 1-75 set
    missing_count = sum(1 for n in range(1, 76) if n not in block_numbers)
    if missing_count != 3:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 3")

    return card_objects


def generate_3_cards_75_25(starting_id: int) -> List[Card75_25]:
    """
    Generates a block of 3 cards ensuring that 72 out of 75 numbers are used.
    This follows the C# logic for balanced distribution across cards.
    """
    card_objects: List[Card75_25] = []
    block_numbers: List[int] = []

    for i in range(3):
        # Initialize the 25-number list for this specific card
        card_numbers = [0] * 25

        # Mapping identical to your C# code (B:1-15, I:16-30, N:31-45, G:46-60, O:61-75)

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[1] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[2] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[3] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[4] = get_non_existent_number(61, 75, block_numbers)

        # ROW 2
        card_numbers[5] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[6] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[7] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[8] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[9] = get_non_existent_number(61, 75, block_numbers)

        # ROW 3 (Central - N column skips the center/Free Space)
        card_numbers[10] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[11] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[12] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[13] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[14] = get_non_existent_number(61, 75, block_numbers)

        # ROW 4
        card_numbers[15] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[16] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[17] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[18] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[19] = get_non_existent_number(61, 75, block_numbers)

        # ROW 5
        card_numbers[20] = get_non_existent_number(1, 15, block_numbers)
        card_numbers[21] = get_non_existent_number(16, 30, block_numbers)
        card_numbers[22] = get_non_existent_number(31, 45, block_numbers)
        card_numbers[23] = get_non_existent_number(46, 60, block_numbers)
        card_numbers[24] = get_non_existent_number(61, 75, block_numbers)

        # Instantiate the Card75_25 class with an incremented ID
        new_card = Card75_25(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 76) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_4_cards_100_25(starting_id: int) -> List[Card100_25]:
    """
    Generates a block of 3 cards ensuring that 72 out of 75 numbers are used.
    This follows the C# logic for balanced distribution across cards.
    """
    card_objects: List[Card100_25] = []
    block_numbers: List[int] = []

    for i in range(4):
        # Initialize the 25-number list for this specific card
        card_numbers = [0] * 25

        # Mapping identical to your C# code (B:1-15, I:16-30, N:31-45, G:46-60, O:61-75)

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[1] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[2] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[3] = get_non_existent_number(61, 80, block_numbers)
        card_numbers[4] = get_non_existent_number(81, 100, block_numbers)

        # ROW 2
        card_numbers[5] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[6] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[7] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[8] = get_non_existent_number(61, 80, block_numbers)
        card_numbers[9] = get_non_existent_number(81, 100, block_numbers)

        # ROW 3 (Central - N column skips the center/Free Space)
        card_numbers[10] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[11] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[12] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[13] = get_non_existent_number(61, 80, block_numbers)
        card_numbers[14] = get_non_existent_number(81, 100, block_numbers)

        # ROW 4
        card_numbers[15] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[16] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[17] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[18] = get_non_existent_number(61, 80, block_numbers)
        card_numbers[19] = get_non_existent_number(81, 100, block_numbers)

        # ROW 5
        card_numbers[20] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[21] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[22] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[23] = get_non_existent_number(61, 80, block_numbers)
        card_numbers[24] = get_non_existent_number(81, 100, block_numbers)

        # Instantiate the Card100_25 class with an incremented ID
        new_card = Card100_25(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 101) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_6_cards_90_15(starting_id: int) -> List[Card90_15]:
    """
    Generates a block of 3 cards ensuring that 72 out of 75 numbers are used.
    This follows the C# logic for balanced distribution across cards.
    """
    card_objects: List[Card90_15] = []
    block_numbers: List[int] = []


    #################### 1
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[1] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[2] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[3] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[4] = get_non_existent_number(70, 79, block_numbers)

    card_numbers[5] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[6] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[7] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[8] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[9] = get_non_existent_number(70, 79, block_numbers)

    card_numbers[10] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[11] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[12] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[13] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[14] = get_non_existent_number(80, 90, block_numbers)

    new_card = Card90_15(card_id=starting_id, numbers_grid=card_numbers)
    card_objects.append(new_card)

    #################### 2
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[1] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[2] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[3] = get_non_existent_number(70, 79, block_numbers)
    card_numbers[4] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[5] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[6] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[7] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[8] = get_non_existent_number(70, 79, block_numbers)
    card_numbers[9] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[10] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[11] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[12] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[13] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[14] = get_non_existent_number(60, 69, block_numbers)

    new_card = Card90_15(card_id=starting_id + 1, numbers_grid=card_numbers)
    card_objects.append(new_card)

    #################### 3
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[1] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[2] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[3] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[4] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[5] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[6] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[7] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[8] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[9] = get_non_existent_number(70, 79, block_numbers)

    card_numbers[10] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[11] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[12] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[13] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[14] = get_non_existent_number(80, 90, block_numbers)

    new_card = Card90_15(card_id=starting_id + 2, numbers_grid=card_numbers)
    card_objects.append(new_card)

    #################### 4
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[1] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[2] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[3] = get_non_existent_number(70, 79, block_numbers)
    card_numbers[4] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[5] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[6] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[7] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[8] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[9] = get_non_existent_number(70, 79, block_numbers)

    card_numbers[10] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[11] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[12] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[13] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[14] = get_non_existent_number(80, 90, block_numbers)

    new_card = Card90_15(card_id=starting_id + 3, numbers_grid=card_numbers)
    card_objects.append(new_card)

    #################### 5
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[1] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[2] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[3] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[4] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[5] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[6] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[7] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[8] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[9] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[10] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[11] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[12] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[13] = get_non_existent_number(70, 79, block_numbers)
    card_numbers[14] = get_non_existent_number(80, 90, block_numbers)

    new_card = Card90_15(card_id=starting_id + 4, numbers_grid=card_numbers)
    card_objects.append(new_card)

    #################### 6
    card_numbers = [0] * 15
    card_numbers[0] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[1] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[2] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[3] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[4] = get_non_existent_number(70, 79, block_numbers)

    card_numbers[5] = get_non_existent_number(1, 9, block_numbers)
    card_numbers[6] = get_non_existent_number(40, 49, block_numbers)
    card_numbers[7] = get_non_existent_number(50, 59, block_numbers)
    card_numbers[8] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[9] = get_non_existent_number(80, 90, block_numbers)

    card_numbers[10] = get_non_existent_number(10, 19, block_numbers)
    card_numbers[11] = get_non_existent_number(20, 29, block_numbers)
    card_numbers[12] = get_non_existent_number(30, 39, block_numbers)
    card_numbers[13] = get_non_existent_number(60, 69, block_numbers)
    card_numbers[14] = get_non_existent_number(70, 79, block_numbers)

    new_card = Card90_15(card_id=starting_id + 5, numbers_grid=card_numbers)
    card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 91) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects
