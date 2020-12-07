import re
from functools import reduce 

def load_bags(file):
    bags = {}
    with open(file) as f:
        for line in f.readlines():
            bag, contents = parse_line(line)
            bags[bag] = contents
    return bags

def parse_line(line):
    groups = re.match(r"(\D+) bags contain", line)
    contents = {}
    for entries in re.findall("(\d+) (\D+) bag", line):
        contents[entries[1]] = int(entries[0])
    return (groups[1], contents)

def can_contain(bags, contents, colour):
    for c in contents.keys():
        if c == colour:
            return True
        elif can_contain(bags, bags[c], colour):
            return True
    return False

def count_containing_bags(bags, target, count_self = False):
    contents = bags[target]

    if contents == {}:
        return 1
    sub_bag_counts = [ value*count_containing_bags(bags, bag, True) for bag, value in contents.items() ]
    if count_self:
        acc = 1
    else:
        acc = 0
    return reduce(lambda acc,x: acc + x, sub_bag_counts, acc )
            

bags = load_bags("input.txt")
part1 = len([ True for bag, contents in bags.items() if can_contain(bags, contents, 'shiny gold') ])
print(f"Part 1 - {part1}")
part2 = count_containing_bags(bags, 'shiny gold')
print(f"Part 2 - {part2}")