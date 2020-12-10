with open('input', 'r') as fd:
    lines = fd.readlines()

SYMBOL_TREE = '#'

rows = list(map(lambda x: x.strip(), lines))
pattern_len = len(rows[0])

num_trees = 0
pos_x = 0

for row in rows:
    encounter = row[pos_x]
    if encounter == SYMBOL_TREE:
        num_trees += 1
    pos_x = (pos_x + 3) % pattern_len

print(num_trees)
