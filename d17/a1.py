from collections import defaultdict
from itertools import product
from typing import Dict, List, Tuple

with open('input', 'r') as fd:
    initial = fd.read().strip().splitlines()


class ConwaySystem:
    INPUT_SPEC_ACTIVE = '#'
    INPUT_SPEC_INACTIVE = '.'
    STAY_ACTIVE_NEIGHBORS = [2, 3]
    BECOME_ACTIVE_NEIGHBORS = [3]

    def __init__(self):
        self.state: Dict[Tuple[int, int, int], bool] = defaultdict(bool)

    def __str__(self):
        perimeter = self.perimeter()
        result = ''
        for x2 in range(perimeter[2][0] + 1, perimeter[2][1]):
            result += f'z={x2}:\n'
            for x1 in range(perimeter[1][0] + 1, perimeter[1][1]):
                for x0 in range(perimeter[0][0] + 1, perimeter[0][1]):
                    result += ConwaySystem.INPUT_SPEC_ACTIVE \
                        if self.state[x0, x1, x2] \
                        else ConwaySystem.INPUT_SPEC_INACTIVE
                result += '\n'
            result += '\n'
        return result

    @staticmethod
    def conway_state_from_char(char: str):
        return char == ConwaySystem.INPUT_SPEC_ACTIVE

    def import_state(self, initial_state: List[str]):
        for x1, line in enumerate(initial_state):
            for x0, char in enumerate(line):
                self.state[x0, x1, 0] = ConwaySystem.conway_state_from_char(char)

    def perimeter(self) -> Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]:
        def dim(d: int):
            return lambda x: x[d]

        active = [x for x, is_active in self.state.items() if is_active]
        return (
            (min(active, key=dim(0))[0] - 1, max(active, key=dim(0))[0] + 1),
            (min(active, key=dim(1))[1] - 1, max(active, key=dim(1))[1] + 1),
            (min(active, key=dim(2))[2] - 1, max(active, key=dim(2))[2] + 1),
        )

    def num_active_neighbors_at(self, x0: int, x1: int, x2: int) -> int:
        neighborhood = filter(lambda x: x != (x0, x1, x2),
                              product(
                                  range(x0 - 1, x0 + 2),
                                  range(x1 - 1, x1 + 2),
                                  range(x2 - 1, x2 + 2),
                              ))
        return sum(1 for n0, n1, n2 in neighborhood if self.state[n0, n1, n2])

    def successor_at(self, x0: int, x1: int, x2: int) -> bool:
        if self.state[x0, x1, x2]:
            return self.num_active_neighbors_at(x0, x1, x2) in ConwaySystem.STAY_ACTIVE_NEIGHBORS
        return self.num_active_neighbors_at(x0, x1, x2) in ConwaySystem.BECOME_ACTIVE_NEIGHBORS

    def iterate(self):
        next_state: Dict[Tuple[int, int, int], bool] = defaultdict(bool)
        perimeter = self.perimeter()
        for x0, x1, x2 in product(
                range(perimeter[0][0], perimeter[0][1] + 1),
                range(perimeter[1][0], perimeter[1][1] + 1),
                range(perimeter[2][0], perimeter[2][1] + 1),
        ):
            next_state[x0, x1, x2] = self.successor_at(x0, x1, x2)
        self.state = next_state

    def count_active_nodes(self):
        return sum(1 for x, is_active in self.state.items() if is_active)


system = ConwaySystem()
system.import_state(initial)
for _ in range(6):
    system.iterate()
print(system.count_active_nodes())
