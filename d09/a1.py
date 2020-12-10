from typing import List, Iterator

LEN_PREAMBLE = 25


def sum_check(n: int, summands: List[int]) -> bool:
    for i, s1 in enumerate(summands):
        for s2 in summands[i + 1:]:
            if s1 + s2 == n:
                return True
    return False


def get_solution(nums: Iterator[int]):
    components = []
    for num in nums:
        if len(components) < LEN_PREAMBLE:
            components.append(num)
            continue
        if not sum_check(num, components):
            return num
        components = components[1:] + [num]


if __name__ == '__main__':
    with open('input', 'r') as fd:
        nums_in = map(int, fd.readlines())
    print(get_solution(nums_in))
