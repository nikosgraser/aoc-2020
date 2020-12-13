from typing import Tuple

with open('input', 'r') as fd:
    lines = fd.readlines()

instructions = [(line[0], int(line[1:])) for line in lines]

CARDINAL_DIRS = {
    'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)
}
TURNING_DIRS = {
    'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
    'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'},
}
FORWARD_DIR = 'F'
Coords = Tuple[int, int]


def turn(start_dir: str, turn_dir: str, degrees: int) -> str:
    result = start_dir
    for _ in range(degrees // 90):
        result = TURNING_DIRS[turn_dir][result]
    return result


def move(start_pos: Coords, ship_facing: str, move_instruction: str, move_value: int) -> Coords:
    if move_instruction == FORWARD_DIR:
        move_instruction = ship_facing
    return (
        start_pos[0] + CARDINAL_DIRS[move_instruction][0] * move_value,
        start_pos[1] + CARDINAL_DIRS[move_instruction][1] * move_value,
    )


position, facing = (0, 0), 'E'
for action, value in instructions:
    if action in TURNING_DIRS:
        facing = turn(facing, action, value)
    else:
        position = move(position, facing, action, value)

print(abs(position[0]) + abs(position[1]))
