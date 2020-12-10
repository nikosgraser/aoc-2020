from sys import exit

from typing import List, Tuple

with open('input', 'r') as fd:
    ops = list(map(lambda x: tuple(x.split()), fd.readlines()))


def run_program(instructions: List[Tuple[str, str]]) -> Tuple[bool, int]:
    """Runs the program contained in `instructions` and returns a tuple
    representing whether it terminates and the value of its accumulator
    immediately before terminating or looping.
    """
    lines_visited = set()
    acc = 0
    ln = 0
    while ln not in lines_visited:
        lines_visited.add(ln)
        if ln >= len(instructions):
            return True, acc
        if instructions[ln][0] == 'jmp':
            ln += int(instructions[ln][1])
            continue
        if instructions[ln][0] == 'acc':
            acc += int(instructions[ln][1])
        ln += 1
    return False, acc


def test_program_fix(instructions: List[Tuple[str, str]], line_to_fix: int, new_instruction: str):
    fixed_instructions = instructions.copy()
    fixed_instructions[line_to_fix] = (new_instruction, fixed_instructions[line_to_fix][1])
    terminated, acc = run_program(fixed_instructions)
    if terminated:
        print(acc)
        exit()


# a1
print(run_program(ops)[1])

# a2
nop_lines = [i for i, op in enumerate(ops) if op[0] == 'nop']
jmp_lines = [i for i, op in enumerate(ops) if op[0] == 'jmp']

for fixed_line in nop_lines:
    test_program_fix(ops, fixed_line, 'jmp')

for fixed_line in jmp_lines:
    test_program_fix(ops, fixed_line, 'nop')
