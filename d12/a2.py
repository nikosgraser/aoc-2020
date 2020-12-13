from typing import Tuple

with open('input', 'r') as fd:
    lines = fd.readlines()

instructions = [(line[0], int(line[1:])) for line in lines]

CARDINAL_DIRS = {
    'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)
}
FORWARD_DIR = 'F'
Coords = Tuple[int, int]


def rotate_wp_90deg(start_wp: Coords, direction: str) -> Coords:
    if direction == 'L':
        return -start_wp[1], start_wp[0]
    else:  # 'R'
        return start_wp[1], -start_wp[0]


def rotate_wp(start_wp: Coords, direction: str, magnitude: int) -> Coords:
    result = start_wp
    for _ in range(magnitude // 90):
        result = rotate_wp_90deg(result, direction)
    return result


def update_wp(start_wp: Coords, direction: str, magnitude: int) -> Coords:
    if direction in CARDINAL_DIRS:
        return (
            start_wp[0] + CARDINAL_DIRS[direction][0] * magnitude,
            start_wp[1] + CARDINAL_DIRS[direction][1] * magnitude,
        )
    return rotate_wp(start_wp, direction, magnitude)


def move(start_pos: Coords, wp: Coords, magnitude: int) -> Coords:
    return (
        start_pos[0] + wp[0] * magnitude,
        start_pos[1] + wp[1] * magnitude,
    )


waypoint = (10, 1)
position = (0, 0)
for action, value in instructions:
    if action != FORWARD_DIR:
        waypoint = update_wp(waypoint, action, value)
    else:
        position = move(position, waypoint, value)

print(abs(position[0]) + abs(position[1]))
