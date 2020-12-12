class Ferry():
    @classmethod
    def read_from_file(cls,file):
        with open(file) as f:
            return cls([ line.strip() for line in f.readlines()])

    def __init__(self, instructions):
        self.instructions = instructions
        self.location = (0,0)

    def navigate(self):
        for instruction in self.instructions:
            self.move(instruction)
        return abs(self.location[0]) + abs(self.location[1])
    
    def move(self, instruction):
        pass

class FerryPart1(Ferry):
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]
    
    def __init__(self, instructions):
        self.dir = 0
        super().__init__(instructions)

    def rotate_right(self, turns):
        self.dir = int((self.dir + turns) % len(self.dirs))
        
    def rotate_left(self, turns):
        self.dir = int((self.dir - turns + len(self.dirs)) % len(self.dirs))
    
    def move_location(self,movement):
         self.location = (self.location[0] + movement[0], self.location[1] + movement[1])

    def move(self, instruction):
        i = instruction[0]
        val = int(instruction[1:])
        actions = {
            'N': lambda x: self.move_location((0,-x)),
            'S': lambda x: self.move_location((0,x)),
            'E': lambda x: self.move_location((x,0)),
            'W': lambda x: self.move_location((-x,0)),
            'R': lambda x: self.rotate_right(x/90),
            'L': lambda x: self.rotate_left(x/90),
            'F': lambda x: self.move_location((self.dirs[self.dir][0]*x, self.dirs[self.dir][1]*x))
        } 
        actions[i](val)
    
class FerryPart2(Ferry):
    
    def __init__(self, instructions):
        self.waypoint = (10, -1)
        super().__init__(instructions)
    
    def rotate_waypoint_right(self, turns):
        for i in range(turns):
            self.waypoint = (-self.waypoint[1], self.waypoint[0])
        
    def rotate_waypoint_left(self, turns):
        for i in range(turns):
            self.waypoint = (self.waypoint[1], -self.waypoint[0])
    
    def move_waypoint(self, dir):        
        self.waypoint = (self.waypoint[0] + dir[0], self.waypoint[1] + dir[1])
    
    def move_location(self, steps):
        self.location = (self.location[0] + self.waypoint[0]*steps, self.location[1] + self.waypoint[1]*steps)

    def move(self, instruction):
        i = instruction[0]
        val = int(instruction[1:])
        actions = {
            'N': lambda x: self.move_waypoint((0,-x)),
            'S': lambda x: self.move_waypoint((0,x)),
            'E': lambda x: self.move_waypoint((x,0)),
            'W': lambda x: self.move_waypoint((-x,0)),
            'R': lambda x: self.rotate_waypoint_right(int(x/90)),
            'L': lambda x: self.rotate_waypoint_left(int(x/90)),
            'F': lambda x: self.move_location(x)
        } 
        actions[i](val)
        

f = FerryPart1.read_from_file("input.txt")
part1 = f.navigate()
print(f"Part1 - {part1}")
f = FerryPart2.read_from_file("input.txt")
part2 = f.navigate()
print(f"Part2 - {part2}")