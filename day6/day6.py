from functools import reduce

def load_group_answers():
    groups = []
    with open("input.txt") as f:
        group = []
        for line in f.readlines():
            if len(line.strip()) == 0:
                groups.append(group)
                group = []
            else:
                group.append(line.strip())
        groups.append(group)
    return groups

def unique_questions(group):
    unique = set()
    for answer in group:
        for char in answer:
            unique.add(char)
    return unique

def all_questions(group):
    questions = [ char for char in group[0] ]
    for answer in group:
        for char in questions.copy():
            if char not in answer:
                questions.remove(char)
    return questions

groups = load_group_answers()
unique_answers_per_group = [ len(unique_questions(group)) for group in groups ]
part1 = reduce(lambda sum,x: sum + x, unique_answers_per_group, 0)
print(f"Part1 - {part1}")
all_questions_per_group = [ len(all_questions(group)) for group in groups ]
part2 = reduce(lambda sum,x: sum + x, all_questions_per_group, 0)
print(f"Part2 - {part2}")
