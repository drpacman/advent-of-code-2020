with open('input') as f:
    values = list(map(int, f.readlines()))
    part1 = set(
        [x*y for x in values for y in values if x+y == 2020]
    ).pop()
    print(f'Part1 - {part1}')
    part2 = set(
        [x*y*z for x in values for y in values for z in values if x+y+z == 2020]
    ).pop()
    print(f'Part2 - {part2}')
