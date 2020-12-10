import re

with open('input', 'r') as fd:
    lines = fd.readlines()

entries = [line.strip() for line in lines]

num_valid = 0

for entry in entries:
    m = re.search(r'^(?P<lower>\d+)-(?P<upper>\d+) (?P<char_spec>[a-z]): (?P<password>[a-z]+)$', entry)
    spec = m.groupdict()
    if int(spec['lower']) <= spec['password'].count(spec['char_spec']) <= int(spec['upper']):
        num_valid += 1

print(num_valid)
