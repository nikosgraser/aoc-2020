import re

from typing import List, Tuple

with open('input', 'r') as fd:
    rules = fd.read().strip().split('\n')

NO_MORE_BAGS = 'no other bags'
START_BAG = 'shiny gold'

container_map = dict()
scanned_containers = set()


def extract_color(bag_spec: str) -> str:
    return re.match(r'^\d+ (.+) bags?$', bag_spec).group(1)


def parse_rule(rule_line: str) -> Tuple[str, List[str]]:
    parts = re.match(r'^(?P<outer>.+?) bags contain (?P<inner>.+?)\.$', rule_line).groupdict()
    outer, all_inner_parts = parts['outer'], parts['inner']
    if all_inner_parts == NO_MORE_BAGS:
        return outer, []

    inner_parts = all_inner_parts.split(', ')
    inner = list(map(extract_color, inner_parts))
    return outer, inner


def count_possible_containers(color: str) -> int:
    if color in scanned_containers:
        return 0
    scanned_containers.add(color)
    if color not in container_map:
        return 1
    return 1 + sum(count_possible_containers(containing_color)
                   for containing_color in container_map[color])


for rule in rules:
    outer_bag, inner_bags = parse_rule(rule)
    for inner_bag in inner_bags:
        if inner_bag not in container_map:
            container_map[inner_bag] = set()
        container_map[inner_bag].add(outer_bag)

# A can be contained in B iff B in container_map[A]
# Minus one since the starting bag doesn't count
print(count_possible_containers(START_BAG) - 1)
