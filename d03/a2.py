with open('input', 'r') as fd:
    lines = list(map(lambda l: l.strip(), fd.readlines()))

SYMBOL_TREE = '#'
PATTERN_LEN = len(lines[0])
X_OFFSETS_1D = [1, 3, 5, 7]
X_OFFSETS_2D = [1]


def count_trees(offset_x: int, offset_y: int) -> int:
    num_trees = 0
    pos_x = 0
    for line in lines[::offset_y]:
        if line[pos_x] == SYMBOL_TREE:
            num_trees += 1
        pos_x = (pos_x + offset_x) % PATTERN_LEN
    return num_trees


result = 1
for x in X_OFFSETS_1D:
    result *= count_trees(
        offset_x=x,
        offset_y=1,
    )
for x in X_OFFSETS_2D:
    result *= count_trees(
        offset_x=x,
        offset_y=2,
    )
print(result)
