def split_input(input):
    sequence = []
    prefix = ''
    for char in input:
        if char == 's' or char == 'n':
            prefix = char
            continue
        sequence.append(prefix + char)
        prefix = ''
    return sequence
         
def read_input(file):
    with open(file) as f:
        return [ split_input(line.strip()) for line in f.readlines() ]

def process(sequences):
    tiles = {}
    for sequence in sequences:
        x = 0
        y = 0
        for entry in sequence:
            if entry == 'e':
                x = x + 2
            elif entry == 'w':
                x = x - 2
            elif 'ne' == entry:
                y = y + 1
                x = x + 1
            elif 'nw' == entry:
                y = y + 1
                x = x - 1
            elif 'se' == entry:
                y = y - 1
                x = x + 1
            elif 'sw' == entry:
                y = y - 1
                x = x - 1
            
        tile = (x,y)
        print(f"Flip {tile}")
        if tile in tiles:
            print(f"Re-flipping {tile}")
            tiles.pop(tile)
        else:
            tiles[tile] = True
    return tiles
    
def apply_end_of_day_rules(tiles):
    next_day_tiles = {}
    additional_tiles_to_check = []
    for x,y in tiles.keys():
        neighbours = [ (x+2,y), (x-2,y), (x+1,y+1), (x-1, y+1), (x+1,y-1), (x-1, y-1) ]
        black_tile_count = 0
        for neighbour in neighbours:
            if neighbour not in tiles:
                additional_tiles_to_check.append(neighbour)
            else:
                black_tile_count = black_tile_count + 1
        if (black_tile_count == 1 or black_tile_count == 2):
            next_day_tiles[ (x,y) ] = True
         
    for x,y in additional_tiles_to_check:
        black_tile_count = 0
        neighbours = [ (x+2,y), (x-2,y), (x+1,y+1), (x-1, y+1), (x+1,y-1), (x-1, y-1) ]
        for neighbour in neighbours:
            if neighbour in tiles:
                black_tile_count = black_tile_count + 1
        if black_tile_count == 2:
            next_day_tiles[ (x,y) ]  = True
    return next_day_tiles
    
if __name__ == '__main__':
    sequence = read_input('input.txt')
    tiles = process(sequence)
    part1 = len(tiles)
    print(f"Part 1 - {part1}")

    for _ in range(100):
        tiles = apply_end_of_day_rules(tiles)
    part2 = len(tiles)
    print(f"Part 2 - {part2}")
