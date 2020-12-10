from typing import List

with open('input', 'r') as fd:
    nums = map(int, fd.readlines())

LEN_PREAMBLE = 25


def sum_check(n: int, summands: List[int]) -> bool:
    for i, s1 in enumerate(summands):
        for s2 in summands[i+1:]:
            if s1 + s2 == n:
                return True
    return False


components = []
for num in nums:
    if len(components) < LEN_PREAMBLE:
        components.append(num)
        continue
    if not sum_check(num, components):
        print(num)
        break
    components = components[1:] + [num]
