from sys import exit

MAGIC_NUMBER = 2020

with open('input', 'r') as fd:
    lines = fd.readlines()

numbers = [int(line.strip()) for line in lines]

numbers_asc = sorted(numbers)
numbers_desc = sorted(numbers, reverse=True)

for n1 in numbers_asc:
    for n2 in numbers_asc:
        if n1 == n2:
            break
        for n3 in numbers_desc:
            if n1 == n3 or n2 == n3:
                break
            if n1 + n2 + n3 == MAGIC_NUMBER:
                print(n1 * n2 * n3)
                exit()
            if n1 + n2 + n3 < MAGIC_NUMBER:
                break
