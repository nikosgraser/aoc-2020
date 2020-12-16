import re
from functools import reduce

from typing import Dict, Iterable, List, Tuple

with open('input', 'r') as fd:
    rules_block, own_ticket_block, nearby_tickets_block = fd.read().split('\n\n')

rules = dict()
for line in rules_block.split('\n'):
    parsed = re.match(
        r'^(?P<field>.+?): (?P<lower1>\d+)-(?P<upper1>\d+) or (?P<lower2>\d+)-(?P<upper2>\d+)$',
        line.strip()
    ).groupdict()
    rules[parsed['field']] = (
        (int(parsed['lower1']), int(parsed['upper1'])),
        (int(parsed['lower2']), int(parsed['upper2'])),
    )

own_ticket = list(map(int, own_ticket_block.split('\n')[1].split(',')))
nearby_tickets = [list(map(int, line.split(','))) for line in nearby_tickets_block.strip().split('\n')[1:]]


def product(it: Iterable[int]) -> int:
    return reduce(lambda x, y: x * y, it, 1)


def matches_rule(value: int, rule: Tuple[Tuple[int, int], Tuple[int, int]]) -> bool:
    return rule[0][0] <= value <= rule[0][1] or rule[1][0] <= value <= rule[1][1]


def matches_any_rule(value: int) -> bool:
    return any(matches_rule(value, rule) for rule in rules.values())


def sum_invalid_values(ticket: List[int]) -> int:
    return sum(value for value in ticket if not matches_any_rule(value))


def is_valid(ticket: List[int]) -> bool:
    return all(matches_any_rule(value) for value in ticket)


# a1
print(sum(sum_invalid_values(ticket) for ticket in nearby_tickets))

# a2
# Step 1: filter for valid tickets
valid_tickets = list(filter(is_valid, nearby_tickets))

# Step 2: Create a list of potential fields for each position in a ticket
field_candidates: Dict[int, List[str]] = dict()
for index in range(len(valid_tickets[0])):
    field_candidates[index] = [
        field for field, rule in rules.items()
        if all(matches_rule(value, rule)
               for value in [ticket[index] for ticket in valid_tickets])
    ]

# Step 3: Eliminate choices by extracting fields that can be matched to exactly 1 index
# Assumption: such fields exist in every iteration
field_mapping: Dict[str, int] = dict()
while len(field_candidates) > 0:
    u_index, u_field = next((index, fields[0])
                            for index, fields in field_candidates.items() if len(fields) == 1)
    field_mapping[u_field] = u_index
    other_indices_with_field = [index for index, fields in field_candidates.items() if u_field in fields]
    for index in other_indices_with_field:
        field_candidates[index].remove(u_field)
    del field_candidates[u_index]

# Solution
print(product(own_ticket[index] for field, index in field_mapping.items() if field.startswith('departure')))
