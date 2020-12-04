import re

with open('input', 'r') as fd:
    lines = fd.readlines()

entries = [line.strip() for line in lines]

num_valid = 0

for entry in entries:
    m = re.search(r'^(?P<first>\d+)-(?P<second>\d+) (?P<char_spec>[a-z]): (?P<password>[a-z]+)$', entry)
    spec = m.groupdict()
    first, second, char_spec, password = int(spec['first']), int(spec['second']), spec['char_spec'], spec['password']
    first_hit = password[first-1] == char_spec
    second_hit = password[second-1] == char_spec
    if (first_hit and not second_hit) or (second_hit and not first_hit):
        num_valid += 1

print(num_valid)
