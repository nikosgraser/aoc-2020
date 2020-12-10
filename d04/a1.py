with open('input', 'r') as fd:
    lines = list(map(lambda x: x.strip(), fd.readlines())) + ['']

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

num_valid = 0
field_collector = set()

for line in lines:
    if len(line) == 0:
        if field_collector >= REQUIRED_FIELDS:
            num_valid += 1
        field_collector = set()

    for field in line.split():
        field_collector.add(field.split(':')[0])

print(num_valid)
