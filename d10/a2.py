with open('input', 'r') as fd:
    adapters = sorted(list(map(int, fd.readlines())))

joltages = [0] + adapters + [max(adapters) + 3]
results = {0: 1}


def num_arrangements(idx: int) -> int:
    if idx not in results:
        predecessors = [idx - i for i in range(1, 4) if
                        idx - i >= 0 and joltages[idx] - joltages[idx - i] <= 3]
        results[idx] = sum(num_arrangements(p) for p in predecessors)
    return results[idx]


print(num_arrangements(len(joltages) - 1))
