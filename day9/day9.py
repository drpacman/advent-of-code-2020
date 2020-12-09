def read_file(file):
    with open(file) as f:
        return [int(line.strip()) for line in f.readlines()]


def is_valid(entries, target):
    for i in range(len(entries)):
        for j in range(i+1, len(entries)):
            # print(i, j, target, entries[i] + entries[j])
            if target != entries[i] + entries[j]:
                continue
            else:
                # print(f"Found {target}")
                return True
    return False
    
def find_invalid(codes, prefix_len):
    total = len(codes)
    prefix = prefix_len
    for k in range(prefix, total):
        if not is_valid(codes[k-prefix:k], codes[k]):
           return codes[k]
    return None

def find_sequence(codes, target):
    for i in range(len(codes)):
        sum = 0
        for j in range(i, len(codes)):
            sum = sum + codes[j]
            if sum == target:
                entries = codes[i:j]
                entries.sort()
                return entries[0] + entries[-1]
            elif sum > target:
                break


codes = read_file('input.txt')    
part1 = find_invalid(codes, 25)
print(f"Part 1 - {part1}")
part2 = find_sequence(codes, part1)
print(f"Part 2 - {part2}")