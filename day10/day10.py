from functools import reduce

def read_input(file):
    with open(file) as f:
        return [ int(line.strip()) for line in f.readlines() ]

def diffs(adapters):
    adapters.sort()
    diffs = {}
    curr = 0
    for adapter in adapters:
        diff = adapter - curr
        if diff in diffs:
            diffs[diff] = diffs[diff] + 1
        else:
            diffs[diff] = 1
        curr = adapter
    return diffs

def get_items_in_runs(adapters):
    curr = 0
    items_in_run=1
    runs = []
    for adapter in adapters:
        if adapter == curr + 1:
            items_in_run = items_in_run + 1
        else:
            runs.append(items_in_run)
            items_in_run = 1
        curr = adapter
    runs.append(items_in_run)
    return runs

def get_combos(n):
    if n > 2:
        return sum(range(n-1))+1
    else:
        return 1    

def count_combinations(adapters):
    acc = 1
    runs = get_items_in_runs(adapters)
    for run in runs:
        if run > 2:
            acc = acc * (sum(range(run-1))+1)
    return acc
    
adapters = read_input('input.txt')
adapters.sort()
results = diffs(adapters)
part1 =  results[1] * (results[3] + 1)
print(f"Part 1 - {part1}")
part2 = count_combinations(adapters)
print(f"Part 2 - {part2}")