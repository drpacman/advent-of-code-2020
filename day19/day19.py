def parse_entry(e):
    if '"' in e:
        return e.split('"')[1]
    return int(e)


def patch_rules(rules):
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return rules

def read_input(file):
    with open(file) as f:
        rules = {}
        entries = []
        readRules = True
        for line in [l.strip() for l in f.readlines()]:
            if readRules and len(line) == 0:
                readRules = False
                continue
            if readRules:
                key_values = line.split(':')
                key = key_values[0]
                values = []
                for entry in key_values[1].strip().split('|'):
                    values.append([parse_entry(i)
                                   for i in entry.strip().split(' ')])
                rules[int(key)] = values
            else:
                entries.append(line)
        return (rules, entries)


def matcher(all_rules):
    def matches_rules(entry):
        matches = match_rules(all_rules[0], all_rules, [(entry, [0])])
        for match in matches:
            remainder, path = match
            if len(remainder) == 0:
                # print(f"Entry {entry} matched path {path}")
                return True
        return False 
               
    return matches_rules


def match_rules(rules, all_rules, entries_with_paths):
    # depth first search
    matches = []    
    for entry_with_path in entries_with_paths:
        list_of_rules = rules
        while len(list_of_rules) > 0:
            rule = list_of_rules[0]
            list_of_rules = list_of_rules[1:]
            results = match_single_rule(rule, all_rules, [entry_with_path] )
            matches =  matches + results
    return matches

def match_single_rule(rule, all_rules, entries_with_paths):
    matches = []
    list_of_elems = rule
    while len(list_of_elems) > 0:
        elem = list_of_elems[0]
        list_of_elems = list_of_elems[1:]
        while len(entries_with_paths) > 0:
            entry, path = entries_with_paths[0]
            entries_with_paths = entries_with_paths[1:]
            if len(entry) == 0:
                continue
            if type(elem) == str:
                if entry[0] != elem:
                    continue
                matches.append((entry[1:], path))
            else:
                child_entries_with_paths = match_rules(all_rules[elem], all_rules, [ (entry, path + [elem]) ])
                if len(child_entries_with_paths) > 0:
                    matches = matches + child_entries_with_paths

        entries_with_paths = matches
        matches = []
    return entries_with_paths

def count_matching_entries(rules, entries):
    return len(list(filter(matcher(rules), entries)))

if __name__ == '__main__':
    rules, entries = read_input('input.txt')
    part1 = count_matching_entries(rules, entries)
    print(f"Part1 - {part1}")
    rules = patch_rules(rules)
    part2 = count_matching_entries(rules, entries)
    print(f"Part2 - {part2}")
