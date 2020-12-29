import re

monster = [
    list("..................0."),
    list("0....00....00....000"),
    list(".0..0..0..0..0..0...")
]

class Tile():

    def __init__(self, tileId, contents):
        self.tileId = tileId
        self.contents = [list(row) for row in contents]
        self.sides = self.generate_sides()

    def __str__(self):
        contents = '\n'.join([''.join(row) for row in self.contents])
        return f"Tile {self.getId()}:\n\n{contents}\n"

    def getId(self):
        return self.tileId

    def count_items(self):
        return sum([1 if elem == '#' else 0 for row in self.contents for elem in row])

    def get_sides(self):
        return [elem for side in self.sides for elem in side]

    def generate_sides(self):
        top = [convert_line_to_number(
            self.contents[0]), convert_line_to_number(self.contents[0][::-1])]
        bottom = [convert_line_to_number(
            self.contents[-1]), convert_line_to_number(self.contents[-1][::-1])]
        temp = [row[0] for row in self.contents]
        left = [convert_line_to_number(temp)]
        temp.reverse()
        left.append(convert_line_to_number(temp))
        temp = [row[-1] for row in self.contents]
        right = [convert_line_to_number(temp)]
        temp.reverse()
        right.append(convert_line_to_number(temp))
        return [top, right, bottom, left]

    def get_pos(self, pos):
        return self.sides[pos][0]

    def get_side_pos(self, side):
        for index, side_variants in self.sides:
            if side in side_variants:
                return index
        return None

    def matches(self, side):
        return side in self.get_sides()

    def get_opposite_side(self, side):
        'Check for a match, and if there is one return the next side to use'
        if self.sides[0][0] == side:
            return self.sides[2][0]
        elif self.sides[0][1] == side:
            return self.sides[2][1]
        elif self.sides[1][0] == side:
            return self.sides[3][0]
        elif self.sides[1][1] == side:
            return self.sides[3][1]
        elif self.sides[2][0] == side:
            return self.sides[0][0]
        elif self.sides[2][1] == side:
            return self.sides[0][1]
        elif self.sides[3][0] == side:
            return self.sides[1][0]
        elif self.sides[3][1] == side:
            return self.sides[1][1]
        return None

    def get_orthogonal_side(self, side):
        if side in self.sides[0]:
            return self.sides[1][0]
        elif side in self.sides[1]:
            return self.sides[2][0]
        elif side in self.sides[2]:
            return self.sides[3][0]
        elif side in self.sides[3]:
            return self.sides[0][0]

    def orientate_to_match_side(self, side, position):
        for index, side_variants in enumerate(self.sides):
            if side in side_variants:
                current = index
                while current != position:
                    self.rotate_right()
                    current = (current + 1) % 4
                if self.sides[position][0] == side:
                    return
                else:
                    if position % 2 == 0:
                        self.flip_horizontal()
                    else:
                        self.flip_vertical()
                return

    def flip_horizontal(self):
        flipped = []
        for row in self.contents:
            flipped.append(row[::-1])
        self.contents = flipped
        self.sides = self.generate_sides()

    def flip_vertical(self):
        flipped = []
        for row in self.contents:
            flipped.insert(0, row)
        self.contents = flipped
        self.sides = self.generate_sides()

    def rotate_right(self):
        rotated = [list(entry) for entry in zip(*self.contents[::-1])]
        self.contents = rotated
        self.sides = self.generate_sides()

    def rotate_left(self):
        for _ in range(3):
            self.rotate_right()

    def get_content_without_borders(self):
        result = []
        rows = self.contents[1:-1]
        for row in rows:
            result.append(row[1:-1])
        return result


def read_tiles(file):
    tiles = []
    contents = []
    tile = 0
    with open(file) as f:
        for entry in [line.strip() for line in f.readlines()]:
            if entry.startswith('Tile'):
                tile = re.match(r"Tile (\d+):", entry)[1]
            elif len(entry) == 0:
                tiles.append(Tile(tile, contents))
                contents = []
            else:
                contents.append(entry)
    tiles.append(Tile(tile, contents))
    return tiles


def convert_line_to_number(line):
    number = 0
    for item in line:
        number = (number << 1)
        if item != '.':
            number = number + 1
    return number


def convert_number_to_line(number):
    line = ''
    for _ in range(10):
        if (number & 1) == 1:
            line = '#' + line
        else:
            line = '.' + line
        number = (number >> 1)
    return line


def find_matched_side_count(tiles):
    matched_sides_by_tile = {}
    for tile in tiles:
        matched_sides = 0
        for side in tile.get_sides():
            for other_tile in tiles:
                if other_tile == tile:
                    continue
                if side in other_tile.get_sides():
                    matched_sides = matched_sides + 1
                    break
        matched_sides_by_tile[tile.getId()] = matched_sides
    return matched_sides_by_tile


def find_corners(tiles):
    matched_by_tile = find_matched_side_count(tiles)
    return [tile_id for tile_id, count in matched_by_tile.items() if count == 4]


def assemble_image(corner_tile_id, tiles):
    corner_tile = [tile for tile in tiles if tile.getId() == corner_tile_id][0]
    unused_tiles = tiles[:]
    unused_tiles.remove(corner_tile)
    # pick the first side to go with
    side = None
    for s in corner_tile.get_sides():
        for tile in unused_tiles:
            if s in tile.get_sides():
                side = s
                break
        if side is not None:
            break

    # start off from top left corner
    corner_tile.orientate_to_match_side(side, 1)
    # make sure bottom of tile matches another tile
    bottom_of_tile_matches = False
    for candidate_tile in unused_tiles:
        if corner_tile.get_pos(2) in candidate_tile.get_sides():
            bottom_of_tile_matches = True
            break
    if bottom_of_tile_matches == False:
        # flip the corner tile vertically so top is at the bottom
        corner_tile.flip_vertical()

    current_tile = corner_tile
    input_side = side
    current_dir = (1, 0)
    x = 0
    y = 0
    max_x = 0
    max_y = 0
    dirs = {
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0)
    }
    output_side_pos_lookup = {
        (1, 0): 1,
        (0, 1): 2,
        (-1, 0): 3,
        (0, -1): 0
    }
    chain = []
    while len(unused_tiles) > 0:
        foundMatch = False
        changeDirection = False
        while foundMatch == False:
            for candidate_tile in unused_tiles:
                if input_side in candidate_tile.get_sides():
                    foundMatch = True
                    break
            if foundMatch == False:
                changeDirection = True
                input_side = current_tile.get_orthogonal_side(input_side)
                        
        current_tile = candidate_tile
        if changeDirection:
            current_dir = dirs[current_dir]
        output_side_pos = output_side_pos_lookup[current_dir]

        dx, dy = current_dir
        x = x + dx
        y = y + dy
        unused_tiles.remove(candidate_tile)
        chain.append((current_tile, output_side_pos, (x, y)))
        input_side = candidate_tile.get_opposite_side(input_side)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    
    image_contents = {(0, 0): corner_tile.get_content_without_borders()}
    last_tile = corner_tile
    for tile, side_pos, coords in chain:
        input_side = last_tile.get_pos(side_pos)
        tile.orientate_to_match_side(input_side, (side_pos + 2) % 4)
        image_contents[coords] = tile.get_content_without_borders()
        last_tile = tile
    image = []
    for y in range(max_y + 1):
        for n in range(8):
            row = []
            for x in range(max_x + 1):
                row = row + image_contents[(x, y)][n]
            image.append(row)
    return Tile("image", image)
      
def insert_monster(image):
    monster_width = len(monster[0])
    monster_height = len(monster)
    image_width = len(image.contents[0])
    image_height = len(image.contents)
    for y in range(image_height - monster_height + 1):
        for x in range(image_width - monster_width + 1):
            found = True
            for index, monster_row in enumerate(monster):
                image_row = image.contents[y + index][x:x+monster_width]
                for col, entry in enumerate(image_row):
                    if monster_row[col] == '0' and entry == '.':
                        found = False
                        break
            if found:
                # replace the monster into the image
                for index, monster_row in enumerate(monster):
                    for col, entry in enumerate(monster_row):
                        if monster_row[col] == '0':
                            image.contents[y+index][x+col] = '0'

def insert_monster_for_image_all_rotations(image):
    insert_monster(image)
    image.rotate_right()
    insert_monster(image)
    image.rotate_right()
    insert_monster(image)
    image.rotate_right()
    insert_monster(image)
    image.rotate_right()
    
def insert_monster_for_image(image):
    insert_monster_for_image_all_rotations(image)
    image.flip_vertical()
    insert_monster_for_image_all_rotations(image)
    image.flip_horizontal()
    insert_monster_for_image_all_rotations(image)
    image.flip_vertical()
    insert_monster_for_image_all_rotations(image)    

if __name__ == '__main__':
    tiles = read_tiles('input.txt')
    corners = find_corners(tiles)
    part1 = 1
    for corner in corners:
        part1 = part1 * int(corner)
    print(f"Part1 - {part1}")
    image = assemble_image(corners[0], tiles)  
    insert_monster_for_image(image)
    print(f"Part2\n")
    print(image)
    part2 = image.count_items()
    print(f"There are {image.count_items()} non-empty items")
    print(f"Part2 - {part2}")
