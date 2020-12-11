class BaseGame():
    entries = []
    width = 0
    height = 0
    moves = [(-1, -1), (0, -1), (1, -1), (-1, 0),
             (1, 0), (-1, 1), (0, 1), (1, 1)]

    def __init__(self, file):
        with open(file) as f:
            self.entries = [[char for char in line.strip()]
                            for line in f.readlines()]
            self.height = len(self.entries)
            self.width = len(self.entries[0])

    def run_iteration(self, max_neighbours):
        next_iteration = [row[:] for row in self.entries]
        changes = 0
        for y in range(self.height):
            for x in range(self.width):
                neighbours = self.count_neighbours(x, y)
                if self.entries[y][x] == '#' and neighbours >= max_neighbours:
                    changes = changes+1
                    next_iteration[y][x] = 'L'
                elif self.entries[y][x] == 'L' and neighbours == 0:
                    changes = changes+1
                    next_iteration[y][x] = '#'
                else:
                    next_iteration[y][x] = self.entries[y][x]
        self.entries = next_iteration
        return changes

    def count_neighbours(self, posX, posY):
        raise Exception("Unimplemented")
    
    def run(self, max_neighbours): 
        while self.run_iteration(max_neighbours) > 0:
            pass

    def count_occupied(self):
        count = 0
        for row in self.entries:
            for char in row:
                if char == '#':
                    count = count + 1
        return count

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.entries])


class GamePart1(BaseGame):
    def count_neighbours(self, posX, posY):
        count = 0
        for (x1, y1) in BaseGame.moves:
            x = posX + x1
            y = posY + y1
            if x >= 0 and x < self.width and y >= 0 and y < self.height:
                if self.entries[y][x] == '#':
                    count = count + 1
        return count

    def run(self):
        super().run(4)


class GamePart2(BaseGame):
    def run(self):
        super().run(5)

    def count_neighbours(self, posX, posY):
        count = 0
        x = posX
        y = posY
        for (x1, y1) in BaseGame.moves:
            x = posX + x1
            y = posY + y1
            while x >= 0 and x < self.width and y >= 0 and y < self.height:
                if self.entries[y][x] == '#':
                    count = count + 1
                    break
                elif self.entries[y][x] != '.':
                    break
                x = x + x1
                y = y + y1

        return count


game_part_1 = GamePart1('input.txt')
game_part_1.run()
print(f"Part 1 - {game_part_1.count_occupied()}")

game_part_2 = GamePart2('input.txt')
game_part_2.run()
print(f"Part 2 - {game_part_2.count_occupied()}")
