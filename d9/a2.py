from a1 import get_solution as a1_solution

with open('input', 'r') as fd:
    nums = list(map(int, fd.readlines()))

TARGET_NUMBER = a1_solution(nums)

summands = []
nums_iter = iter(nums)

while sum(summands) != TARGET_NUMBER:
    if sum(summands) < TARGET_NUMBER:
        summands.append(next(nums_iter))
    else:
        summands = summands[1:]

print(min(summands) + max(summands))
