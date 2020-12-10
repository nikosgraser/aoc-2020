with open('input', 'r') as fd:
    ops = list(map(lambda x: x.split(), fd.readlines()))

lines_visited = set()
acc = 0
ln = 0
while ln not in lines_visited:
    lines_visited.add(ln)
    if ops[ln][0] == 'jmp':
        ln += int(ops[ln][1])
        continue
    if ops[ln][0] == 'acc':
        acc += int(ops[ln][1])
    ln += 1

print(acc)
