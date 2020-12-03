
def isTree(forest, x, y):
    pos = x % (len(forest[0]) - 1)
    return forest[y][pos] == '#'


def countTrees(forest, incx, incy):
    x = y = count = 0
    while y < len(forest):
        if isTree(forest, x, y):
            count = count + 1
        x = x + incx
        y = y + incy
    return count


def calculate(target, slopes):
    product = 1
    with open(target) as file:
        forest = list(file.readlines())
        for slope in slopes:
            product = product * countTrees(forest, *slope)
    return product

part1 = calculate('input.txt', [(3,1)])
print(f"Part 1 - {part1}")
part2 = calculate('input.txt', [(1, 1), (3, 1), (5, 1), (7, 1),(1, 2)])
print(f"Part 2 - {part2}")
