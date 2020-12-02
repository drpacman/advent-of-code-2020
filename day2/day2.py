import re


def parse_line(line):
    result = re.match(r'(\d+)-(\d+) (\D): (\D+)', line)
    start = int(result.group(1))
    end = int(result.group(2))
    char = result.group(3)
    password = result.group(4)
    return (start, end, char, password)


def check_password_part1(minNum, maxNum, char, password):
    count = len([c for c in password if c == char])
    return count >= minNum and count <= maxNum


def check_password_part2(firstPos, secondPos, char, password):
    return (password[firstPos - 1] == char) ^ (password[secondPos - 1] == char)


with open('input.txt') as f:
    entries = [parse_line(line) for line in f.readlines()]
    part1 = [entry[3] for entry in entries if check_password_part1(*entry)]
    print(f"Part1 - {len(part1)}")
    part2 = [entry[3] for entry in entries if check_password_part2(*entry)]
    print(f"Part2 - {len(part2)}")
