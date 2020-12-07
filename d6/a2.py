with open('input', 'r') as fd:
    groups = fd.read().strip().split('\n\n')


def count_shared_chars(raw_grp: str) -> int:
    grp = raw_grp.split('\n')
    return sum(1 if all(c in answer for answer in grp) else 0 for c in grp[0])


print(sum(count_shared_chars(group) for group in groups))
