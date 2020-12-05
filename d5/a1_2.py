from itertools import count
from sys import exit
from typing import Tuple

with open('input', 'r') as fd:
    raw_passes = fd.read().split('\n')
passes = filter(lambda p: len(p) > 0, raw_passes)


def decode_pass(encoded: str) -> Tuple[int, int]:
    row_spec, column_spec = encoded[:7][::-1], encoded[7:][::-1]
    row = sum(2 ** i if row_spec[i] == 'B' else 0 for i in range(len(row_spec)))
    column = sum(2 ** i if column_spec[i] == 'R' else 0 for i in range(len(column_spec)))
    return row, column


def pass_seatid(decoded: Tuple[int, int]) -> int:
    return decoded[0] * 8 + decoded[1]


all_seat_numbers = [pass_seatid(decode_pass(bpass)) for bpass in passes]

# a1
print(max(all_seat_numbers))

# a2
for candidate in count(min(all_seat_numbers)):
    if candidate not in all_seat_numbers:
        print(candidate)
        exit()
