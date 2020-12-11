from typing import List

with open('input', 'r') as fd:
    rows = list(map(lambda x: x.strip(), fd.readlines()))

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'
NUM_ROWS = len(rows)
NUM_COLS = len(rows[0])


def symbol_at(i: int, j: int, seats: List[str]) -> str:
    if 0 <= i < NUM_COLS and 0 <= j < NUM_ROWS:
        return seats[j][i]
    return EMPTY


def is_occupied_in_direction(i: int, j: int, dir_i: int, dir_j: int, seats: List[str]) -> bool:
    next_i, next_j = i + dir_i, j + dir_j
    while symbol_at(next_i, next_j, seats) == FLOOR:
        next_i, next_j = next_i + dir_i, next_j + dir_j
    return symbol_at(next_i, next_j, seats) == OCCUPIED


def count_occupied_around(i: int, j: int, seats: List[str]) -> int:
    directions = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1),
    ]
    return sum([1 for dir_i, dir_j in directions if is_occupied_in_direction(i, j, dir_i, dir_j, seats)])


def the_next_generation(seats: List[str]) -> List[str]:
    seats_ng = [''] * NUM_ROWS
    for j in range(NUM_ROWS):
        for i in range(NUM_COLS):
            num_visible_occupied = count_occupied_around(i, j, seats)
            if seats[j][i] == EMPTY and num_visible_occupied == 0:
                seats_ng[j] += OCCUPIED
            elif seats[j][i] == OCCUPIED and num_visible_occupied >= 5:
                seats_ng[j] += EMPTY
            else:
                seats_ng[j] += seats[j][i]
    return seats_ng


tpg = []
tcg = rows
while tcg != tpg:
    tpg, tcg = tcg, the_next_generation(tcg)

print(sum(sum(1 for seat in row if seat == OCCUPIED) for row in tcg))
