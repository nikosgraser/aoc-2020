import re
from functools import reduce

with open('input', 'r') as fd:
    instructions = map(lambda l: l.strip().split(' = '), fd.readlines())


def apply_mask(mask: str, value: int) -> int:
    value_bin = bin(value)[2:].zfill(36)
    return int(reduce(
        lambda x, y: x + y,
        [mask[i] if mask[i] != 'X' else value_bin[i] for i in range(len(mask))]
    ), base=2)


memory = dict()
write_mask = 'X' * 36
for instruction in instructions:
    if instruction[0] == 'mask':
        write_mask = instruction[1]
        continue
    address = re.match(r'mem\[(\d+)\]', instruction[0]).group(1)
    memory[address] = apply_mask(write_mask, int(instruction[1]))

print(sum(v for v in memory.values()))
