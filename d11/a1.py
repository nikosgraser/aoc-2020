from typing import List

with open('input', 'r') as fd:
    rows = list(map(lambda x: x.strip(), fd.readlines()))

OCCUPIED = '#'
EMPTY = 'L'
FLOOR = '.'
NUM_ROWS = len(rows)
NUM_COLS = len(rows[0])


def is_occupied_at(i: int, j: int, seats: List[str]) -> bool:
    if 0 <= i < NUM_COLS and 0 <= j < NUM_ROWS:
        return seats[j][i] == OCCUPIED
    return False


def count_occupied_around(i: int, j: int, seats: List[str]) -> int:
    adjacent = [
        (i - 1, j - 1), (i, j - 1), (i + 1, j - 1),
        (i - 1, j), (i + 1, j),
        (i - 1, j + 1), (i, j + 1), (i + 1, j + 1),
    ]
    return sum([1 for i, j in adjacent if is_occupied_at(i, j, seats)])


def the_next_generation(seats: List[str]) -> List[str]:
    seats_ng = [''] * NUM_ROWS
    for j in range(NUM_ROWS):
        for i in range(NUM_COLS):
            num_neighbours = count_occupied_around(i, j, seats)
            if seats[j][i] == EMPTY and num_neighbours == 0:
                seats_ng[j] += OCCUPIED
            elif seats[j][i] == OCCUPIED and num_neighbours >= 4:
                seats_ng[j] += EMPTY
            else:
                seats_ng[j] += seats[j][i]
    return seats_ng


tpg = []
tcg = rows
while tcg != tpg:
    tpg, tcg = tcg, the_next_generation(tcg)

print(sum(sum(1 for seat in row if seat == OCCUPIED) for row in tcg))
