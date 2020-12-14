import re
from functools import reduce
from itertools import product

from typing import List, Tuple

with open('input', 'r') as fd:
    instructions = map(lambda l: l.strip().split(' = '), fd.readlines())

X = 'X'


def apply_floating_sequence(value: str, sequence: Tuple[str]) -> str:
    result = value
    for c in sequence:
        result = result.replace(X, c, 1)
    return result


def get_floating_addresses(mask: str, value: int) -> List[int]:
    value_bin = bin(value)[2:].zfill(36)
    masked_value = reduce(
        lambda x, y: x + y,
        [mask[i] if mask[i] != '0' else value_bin[i] for i in range(len(mask))]
    )
    sequences = product('01', repeat=masked_value.count(X))
    return [int(apply_floating_sequence(masked_value, sequence)) for sequence in sequences]


memory = dict()
write_mask = X * 36
for instruction in instructions:
    if instruction[0] == 'mask':
        write_mask = instruction[1]
        continue
    address_from_instr = re.match(r'mem\[(\d+)\]', instruction[0]).group(1)
    addresses_to_write = get_floating_addresses(write_mask, int(address_from_instr))
    for address in addresses_to_write:
        memory[address] = int(instruction[1])

print(sum(memory.values()))
