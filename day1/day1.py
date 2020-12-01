def find_value(values, depth, value=0):
    if depth == 1:
        for v in values:
            if value + v == 2020:
                return v
        return -1
    else:
        for v in values:
            product = find_value(values, depth - 1, v+value)
            if product > 0:
                return product * v
        return -1

with open('input') as f:
    values =  list(map(int, f.readlines()))
    print(f'Part1 - {find_value(values, 2)}')
    print(f'Part2 - {find_value(values, 3)}')
