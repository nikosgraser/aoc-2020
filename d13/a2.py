from typing import Iterable, Tuple
from functools import reduce

with open('input', 'r') as fd:
    bus_lines_raw = fd.readlines()[1].strip().split(',')

bus_lines = list(map(int, filter(lambda bl: bl != 'x', bus_lines_raw)))
bl_offsets = [i for i, n in enumerate(bus_lines_raw) if n != 'x']


def product(it: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, it, 1)


def bezout_coeff(a: int, b: int) -> Tuple[int, int]:
    r0, r1 = a, b
    s0, s1 = 1, 0
    t0, t1 = 0, 1
    while r1 != 0:
        q = r0 // r1
        r0, r1 = r1, r0 - q*r1
        s0, s1 = s1, s0 - q*s1
        t0, t1 = t1, t0 - q*t1
    return s0, t0


# For an explanation of how this works, look up the Chinese Remainder Theorem, e.g.:
# https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Existence_(direct_construction)
N = product(bus_lines)
result = 0
for i in range(len(bus_lines)):
    a_i = bus_lines[i] - bl_offsets[i]
    n_i = bus_lines[i]
    N_i = N // n_i  # Using a float value here with N / n_i results in overflow errors for high numbers
    M_i, _ = bezout_coeff(N_i, n_i)
    result += a_i * M_i * N_i

# This calculation finds _a_ solution - other solutions are obtained by adding multiples of N.
# We are interested in the smallest positive solution.
result %= N

print(result)
