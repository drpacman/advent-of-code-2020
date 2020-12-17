def read_input(file, dimensions):
    with open(file) as f:
        grid = {}
        additional_dims = [0] * (dimensions - 2)
        entries = [[ char for char in line ] for line in f.readlines()]
        for y, entry in enumerate(entries):
            for x, entry in enumerate(entry):
                if entry == '#':
                    grid[ tuple( [x, y] + additional_dims ) ] = True
        return grid

def create_keys(dimensions, mins, maxs):
    for dim in range(dimensions):
        next = []                                
        for val in range(mins[dim] - 1, maxs[dim] + 2):
            if dim == 0:
                next.append(val)
            else:
                for key in keys:
                    next.append(create_key(val, key))
        keys = next
    return keys

def create_key( dimension, existing ):
    if type(existing) == tuple:
        return tuple(list(existing) + [dimension])
    else:
        return (existing, dimension)

def count_neighbours(key, input):
    dimensions = len(key)
    keys = create_keys(dimensions, key, key)    
    count = 0
    for k in keys:
        if k == key:
            continue
        entry = input.get(k, False)
        if entry == True:
            count = count + 1
    return count

def run_cycles(input, loops):
    if loops > 0:
        return run_cycles(run_cycle(input), loops - 1)
    return input

def run_cycle(input):
    dimensions = len(list(input.keys())[0])
    mins = [0] * dimensions
    maxs = [0] * dimensions
    for dim in range(dimensions):
        mins[dim] = min([ key[dim] for key in input.keys() ])
        maxs[dim] = max([ key[dim] for key in input.keys() ])
    keys = keys = create_keys(dimensions, mins, maxs)    
    
    result = {}
    for key in keys:
        c = count_neighbours(key, input)
        if key in input:
            if (c == 2 or c ==3):
                result[key] = True
        elif c == 3: 
            result[key] = True
    return result    

input = read_input('input.txt', 3)
result = run_cycles(input, 6)  
print(f"Part 1 - {len(result)}") 
input = read_input('input.txt', 4)
result = run_cycles(input, 6)  
print(f"Part 2 - {len(result)}") 
