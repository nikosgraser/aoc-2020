with open('input', 'r') as fd:
    groups = fd.read().strip().split('\n\n')


def count_unique_chars(grp: str) -> int:
    return len(set(grp.replace('\n', '')))


print(sum(count_unique_chars(group) for group in groups))
