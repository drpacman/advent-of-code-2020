
def play(seq, max):
    seen = {}
    turn = len(seq) + 1
    for index, item in enumerate(seq):
        seen[item] = [index + 1]
    last = seq[-1]
    while turn <= max:
        if last in seen:
            occurances = seen[last]
            occurances.append(turn-1)
            last = occurances[-1] - occurances[-2]
        else:
            seen[last] = [turn - 1]
            last = 0        
        turn = turn + 1
    return last

print(f"Part1 - {play([6,19,0,5,7,13,1], 2020)}")
print(f"Part2 - {play([6,19,0,5,7,13,1], 30000000)}")