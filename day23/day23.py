def move(puzzle, rounds):
    max_value = max(puzzle)
    # create dictionary keyed by item pointing to next item
    lookup = dict(zip(puzzle, puzzle[1:]))
    lookup[puzzle[-1]] = puzzle[0]
    current = puzzle[0]

    for _ in range(rounds):
        moved = [lookup[current]]
        moved.append(lookup[moved[-1]])
        moved.append(lookup[moved[-1]])

        next = current
        while True:
            next = next - 1 if next > 1 else max_value
            if next in moved:
                continue
            break
        temp = lookup[next]
        lookup[current] = lookup[moved[-1]]
        lookup[next] = moved[0]
        lookup[moved[-1]] = temp
        current = lookup[current]
    return lookup


puzzle = [int(value) for value in '318946572']
lookup_table = move(puzzle, 100)
value = 1
result = []
while True:
    value = lookup_table[value]
    if value == 1:
        break
    result.append(value)
part1 = ''.join([ str(i) for i in result ])
print(f"Puzzle after part1 - {part1}")

puzzle = [ int(value) for value in '318946572' ]
puzzle = puzzle[:] + [ x for x in range(10, 1000001) ]
lookup_table = move(puzzle, 10000000)
x = lookup_table[1]
y = lookup_table[x]
print(f"Puzzle after part2 - {x*y}")
