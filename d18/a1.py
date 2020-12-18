from typing import Tuple

with open('input', 'r') as fd:
    lines = [line.strip().replace(' ', '') for line in fd.readlines()]

PAREN_OPEN = '('
PAREN_CLOSE = ')'
DIGITS = '0123456789'
ADD = '+'
MULT = '*'
SET = '='


def apply_operator(operator: str, left: int, right: int):
    if operator == ADD:
        return left + right
    if operator == MULT:
        return left * right
    # SET
    return right


def eval_expression(line: str, start_index: int) -> Tuple[int, int]:
    value, cursor = 0, start_index
    operator = SET
    while cursor < len(line) and line[cursor] != PAREN_CLOSE:
        c = line[cursor]
        if c == PAREN_OPEN:
            expr_value, cursor = eval_expression(line, cursor + 1)
            value = apply_operator(operator, value, expr_value)
        elif c in DIGITS:
            value, cursor = apply_operator(operator, value, int(c)), cursor + 1
        elif c in (ADD, MULT):
            operator, cursor = c, cursor + 1
    return value, cursor + 1


print(sum(eval_expression(line, 0)[0] for line in lines))
