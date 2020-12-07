import re

from typing import Dict, List, Tuple

with open('input', 'r') as fd:
    rules = fd.read().strip().split('\n')

NO_MORE_BAGS = 'no other bags'
START_BAG = 'shiny gold'

# e.g.
# {
#   'light red': [
#     (1, 'bright white'),
#     (2, 'muted yellow')
#   ]
# }
container_map: Dict[str, List[Tuple[int, str]]] = dict()
known_contents: Dict[str, int] = dict()


def extract_count_and_color(bag_spec: str) -> Tuple[int, str]:
    m = re.match(r'^(\d+) (.+) bags?$', bag_spec)
    return int(m.group(1)), m.group(2)


def parse_rule(rule_line: str) -> Tuple[str, List[Tuple[int, str]]]:
    parts = re.match(r'^(?P<outer>.+?) bags contain (?P<inner>.+?)\.$', rule_line).groupdict()
    outer, all_inner_parts = parts['outer'], parts['inner']
    if all_inner_parts == NO_MORE_BAGS:
        return outer, []

    inner_parts = all_inner_parts.split(', ')
    inner = list(map(extract_count_and_color, inner_parts))
    return outer, inner


def count_contained_bags(color: str) -> int:
    if color not in known_contents:
        if color not in container_map:
            known_contents[color] = 1
        else:
            known_contents[color] = 1 + sum(num_bags_of_type * count_contained_bags(bag_type)
                                            for num_bags_of_type, bag_type in container_map[color])
    return known_contents[color]


for rule in rules:
    outer_bag, inner_bags = parse_rule(rule)
    container_map[outer_bag] = inner_bags

# A contains n bags of color B iff (n, B) in container_map[A]
# Minus one since the starting bag doesn't count
print(count_contained_bags(START_BAG) - 1)
