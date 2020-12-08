import re


def parse_file(file):
    with open(file) as f:
        return [parse_instruction(line) for line in f.readlines()]


def parse_instruction(line):
    groups = re.match(r"([a-z]{3}) ([+-]+\d+)", line)
    return (groups[1], int(groups[2]))


def handle_instruction(instructions, pc, acc):
    opcode, value = instructions[pc]
    if opcode == 'acc':
        acc = acc + value
        pc = pc + 1
    elif opcode == 'jmp':
        pc = pc + value
    else:
        pc = pc + 1
    return (pc, acc)


def run_program(instructions):
    pc = 0
    acc = 0
    visited = set()
    while pc not in visited and pc < len(instructions):
        visited.add(pc)
        pc, acc = handle_instruction(instructions, pc, acc)

    return (acc, pc >= len(instructions))


def find_terminating_instruction(instructions):
    for index, instr in enumerate(instructions):
        if instr == 'acc':
            continue
        modification = 'nop'
        if instr == 'nop':
            modification = 'jmp'

        modified_instructions = instructions.copy()
        modified_instructions[index] = (
            modification, modified_instructions[index][1])
        acc, terminated = run_program(modified_instructions)
        if terminated:
            return acc


instructions = parse_file("input.txt")
part1, _ = run_program(instructions)
print(f"Part 1 - {part1}")
part2 = find_terminating_instruction(instructions)
print(f"Part 2 - {part2}")
