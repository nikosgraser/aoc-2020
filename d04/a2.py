import re

with open('input', 'r') as fd:
    lines = list(map(lambda x: x.strip(), fd.readlines())) + ['']

REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


def validate_required_fields(fields: dict) -> bool:
    if not set(fields.keys()) >= REQUIRED_FIELDS:
        return False
    byr, iyr, eyr, hgt, hcl, ecl, pid = fields['byr'], fields['iyr'], fields['eyr'], fields['hgt'], \
                                        fields['hcl'], fields['ecl'], fields['pid']
    if not (re.match(r'^\d{4}$', byr) and 1920 <= int(byr) <= 2002):
        return False
    if not (re.match(r'^\d{4}$', iyr) and 2010 <= int(iyr) <= 2020):
        return False
    if not (re.match(r'^\d{4}$', eyr) and 2020 <= int(eyr) <= 2030):
        return False
    m = re.match(r'^(?P<num>\d+)(?P<unit>cm|in)$', hgt)
    if not m:
        return False
    hgt_parts = m.groupdict()
    if hgt_parts['unit'] == 'cm' and not (150 <= int(hgt_parts['num']) <= 193):
        return False
    if hgt_parts['unit'] == 'in' and not (59 <= int(hgt_parts['num']) <= 76):
        return False
    if not re.match(r'^#[0-9a-f]{6}$', hcl):
        return False
    if ecl not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        return False
    if not re.match(r'^\d{9}$', pid):
        return False
    return True


num_valid = 0
field_collector = dict()

for line in lines:
    if len(line) == 0:
        if validate_required_fields(field_collector):
            num_valid += 1
        field_collector = dict()

    for field in line.split():
        field_collector[field.split(':')[0]] = field.split(':')[1]

print(num_valid)
