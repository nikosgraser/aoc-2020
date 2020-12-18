import re
from math import prod

from typing import Callable

with open('input', 'r') as fd:
    lines = [line.strip().replace(' ', '') for line in fd.readlines()]

PAREN_OPEN = '('
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


def eval_simple_no_precedence_rules(expr: str) -> int:
    cursor, value = 0, 0
    operator = SET
    while cursor < len(expr):
        c = expr[cursor]
        if c in DIGITS:
            while cursor + 1 < len(expr) and expr[cursor + 1] in DIGITS:
                c += expr[cursor + 1]
                cursor += 1
            value = apply_operator(operator, value, int(c))
        elif c in (ADD, MULT):
            operator = c
        cursor += 1
    return value


def eval_simple_add_before_mult(expr: str) -> int:
    return prod(sum(int(summand) for summand in factor.split(ADD)) for factor in expr.split(MULT))


def eval_complex(expr: str, eval_simple: Callable[[str], int]) -> int:
    result = expr
    while PAREN_OPEN in result:
        innermost_parens = re.findall(r'(\([0-9*+]+\))', result)
        for match in innermost_parens:
            result = result.replace(match, str(eval_simple(match[1:-1])))
    return eval_simple(result)


# a1
print(sum(eval_complex(line, eval_simple_no_precedence_rules) for line in lines))
# a2
print(sum(eval_complex(line, eval_simple_add_before_mult) for line in lines))
