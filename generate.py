import random
import time
from itertools import chain
from typing import List

from Classes import BaseCard, Card60_20, Card100_25, Card75_24, Card75_25, Card80_16, Card90_15, Card30_09
from global_var import GV, TournamentType


def generate_tournament_cards(total_needed: int, no_same_position: bool, no_different_position: bool) -> int:
    all_cards: List[BaseCard] = []
    max_card_id: int = 0

    if GV.tournament_cards:
        max_card_id = max(GV.tournament_cards, key=lambda card: card.card_id).card_id

    max_card_id += 1
    start_from = max_card_id

    print(f"Generating {total_needed} cards, starting from {max_card_id}")
    if no_same_position:
        print("Prevent identical cards (same numbers, same positions)")
    if no_different_position:
        print("Prevent cards with the same set of numbers, regardless of position")

    start = time.time()
    print("Start:", start)

    while len(all_cards) < total_needed:
        block = None

        if GV.tournament_type == TournamentType.BINGO_30_09:
            block = generate_3_cards_30_09(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_60_20:
            block = generate_3_cards_60_20(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_75_24:
            block = generate_3_cards_75_24(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_75_25:
            block = generate_3_cards_75_25(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_80_16:
            block = generate_5_cards_80_16(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_90_15:
            block = generate_6_cards_90_15(starting_id=max_card_id)

        if GV.tournament_type == TournamentType.BINGO_100_25:
            block = generate_4_cards_100_25(starting_id=max_card_id)

        #### if there is a problem invalidate all block
        error = False

        if no_same_position or no_different_position:
            for card in block:
                for other in chain(all_cards, GV.tournament_cards):
                    if no_same_position and card.numbers_in_sequence_equal_to(other):
                        print(f"Same pos: {card.card_id} = {other.card_id}")
                        print(f"Num{card.card_id}: {card.numbers_grid} Sum: {card._sum}")
                        print(f"Num{other.card_id}: {other.numbers_grid} Sum: {other._sum}")

                        error = True
                        break
                    if no_different_position and card.numbers_not_in_sequence_equal_to(other):
                        print(f"Diff pos: {card.card_id} = {other.card_id}")
                        print(f"Num{card.card_id}: {card.numbers_grid} Sum: {card._sum}")
                        print(f"Num{other.card_id}: {other.numbers_grid} Sum: {other._sum}")

                        error = True
                        break

                if error:
                    break

        if not error:
            max_card_id += len(block)
            all_cards.extend(block)
            # print(f"Added {len(block)} cards to pool of {len(all_cards)} cards for {total_needed}")

    end = time.time()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:.2f} seconds")

    GV.tournament_cards.extend(all_cards)
    return max_card_id - start_from


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


def generate_3_cards_30_09(starting_id: int) -> List[Card30_09]:
    card_objects: List[Card30_09] = []
    block_numbers: List[int] = []

    for i in range(3):
        card_numbers = [0] * 9

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 10, block_numbers)
        card_numbers[1] = get_non_existent_number(11, 20, block_numbers)
        card_numbers[2] = get_non_existent_number(21, 30, block_numbers)

        card_numbers[3] = get_non_existent_number(1, 10, block_numbers)
        card_numbers[4] = get_non_existent_number(11, 20, block_numbers)
        card_numbers[5] = get_non_existent_number(21, 30, block_numbers)

        card_numbers[6] = get_non_existent_number(1, 10, block_numbers)
        card_numbers[7] = get_non_existent_number(11, 20, block_numbers)
        card_numbers[8] = get_non_existent_number(21, 30, block_numbers)

        new_card = Card30_09(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 31) if n not in block_numbers)
    if missing_count != 3:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 3")

    return card_objects


def generate_3_cards_60_20(starting_id: int) -> List[Card60_20]:
    card_objects: List[Card60_20] = []
    block_numbers: List[int] = []

    for i in range(3):
        card_numbers = [0] * 20

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 12, block_numbers)
        card_numbers[1] = get_non_existent_number(13, 24, block_numbers)
        card_numbers[2] = get_non_existent_number(25, 36, block_numbers)
        card_numbers[3] = get_non_existent_number(37, 48, block_numbers)
        card_numbers[4] = get_non_existent_number(49, 60, block_numbers)

        # ROW 2
        card_numbers[5] = get_non_existent_number(1, 12, block_numbers)
        card_numbers[6] = get_non_existent_number(13, 24, block_numbers)
        card_numbers[7] = get_non_existent_number(25, 36, block_numbers)
        card_numbers[8] = get_non_existent_number(37, 48, block_numbers)
        card_numbers[9] = get_non_existent_number(49, 60, block_numbers)

        # ROW 3
        card_numbers[10] = get_non_existent_number(1, 12, block_numbers)
        card_numbers[11] = get_non_existent_number(13, 24, block_numbers)
        card_numbers[12] = get_non_existent_number(25, 36, block_numbers)
        card_numbers[13] = get_non_existent_number(37, 48, block_numbers)
        card_numbers[14] = get_non_existent_number(49, 60, block_numbers)

        # ROW 4
        card_numbers[15] = get_non_existent_number(1, 12, block_numbers)
        card_numbers[16] = get_non_existent_number(13, 24, block_numbers)
        card_numbers[17] = get_non_existent_number(25, 36, block_numbers)
        card_numbers[18] = get_non_existent_number(37, 48, block_numbers)
        card_numbers[19] = get_non_existent_number(49, 60, block_numbers)

        new_card = Card60_20(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 61) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_3_cards_75_24(starting_id: int) -> List[Card75_24]:
    card_objects: List[Card75_24] = []
    block_numbers: List[int] = []

    for i in range(3):
        card_numbers = [0] * 24

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

        new_card = Card75_24(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 76) if n not in block_numbers)
    if missing_count != 3:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 3")

    return card_objects


def generate_3_cards_75_25(starting_id: int) -> List[Card75_25]:
    card_objects: List[Card75_25] = []
    block_numbers: List[int] = []

    for i in range(3):
        card_numbers = [0] * 25

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

        new_card = Card75_25(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 76) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_5_cards_80_16(starting_id: int) -> List[Card80_16]:
    card_objects: List[Card80_16] = []
    block_numbers: List[int] = []

    for i in range(5):
        card_numbers = [0] * 16

        # ROW 1
        card_numbers[0] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[1] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[2] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[3] = get_non_existent_number(61, 80, block_numbers)

        # ROW 2
        card_numbers[4] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[5] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[6] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[7] = get_non_existent_number(61, 80, block_numbers)

        # ROW 3
        card_numbers[8] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[9] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[10] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[11] = get_non_existent_number(61, 80, block_numbers)

        # ROW 4
        card_numbers[12] = get_non_existent_number(1, 20, block_numbers)
        card_numbers[13] = get_non_existent_number(21, 40, block_numbers)
        card_numbers[14] = get_non_existent_number(41, 60, block_numbers)
        card_numbers[15] = get_non_existent_number(61, 80, block_numbers)

        new_card = Card80_16(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 81) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_4_cards_100_25(starting_id: int) -> List[Card100_25]:
    card_objects: List[Card100_25] = []
    block_numbers: List[int] = []

    for i in range(4):
        card_numbers = [0] * 25

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

        new_card = Card100_25(card_id=starting_id + i, numbers_grid=card_numbers)
        card_objects.append(new_card)

    missing_count = sum(1 for n in range(1, 101) if n not in block_numbers)
    if missing_count != 0:
        raise Exception(f"Generation Error: {missing_count} numbers missing instead of 0")

    return card_objects


def generate_6_cards_90_15(starting_id: int) -> List[Card90_15]:
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
