with open('input', 'r') as fd:
    starting_numbers = [int(n) for n in fd.read().split(',')]


def get_num_in_turn(target_turn: int) -> int:
    last_seen = dict()
    for i, num in enumerate(starting_numbers):
        last_seen[num] = i + 1  # turns start counting at 1

    current_num = starting_numbers[-1]
    start_turn = len(starting_numbers)

    for turn in range(start_turn, target_turn):
        if current_num not in last_seen:
            last_seen[current_num], current_num = turn, 0
            continue
        last_seen[current_num], current_num = turn, turn - last_seen[current_num]

    return current_num


# a1
print(get_num_in_turn(2020))
# a2
print(get_num_in_turn(30_000_000))
