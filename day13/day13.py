def read_timetable(file):
    with open(file) as f:
        start_time = int(f.readline().strip())
        buses = [ int(val) for val in f.readline().strip().split(',') if val != 'x' ]
        return (start_time, buses)

def pick_bus(start_time, buses):
    now = start_time
    while True:
        for bus in buses:
            if now % bus == 0:
                return (bus, now - start_time)
        now = now + 1
    return ( None, None )

def read_bus_positions(file):
    with open(file) as f:
        f.readline()
        buses = {}
        for index,val in enumerate(f.readline().strip().split(',')):
            if val != 'x':
                buses[index] = int(val)
        return buses

def check_timestamp(t, buses):
    for key, value in buses.items():
        if (t + key) % value != 0:
            return False
    return True

def find_timestamp(buses):
    timestamp = buses[0]
    while True:
        if check_timestamp(timestamp, buses):
            return timestamp
        else:
            timestamp = timestamp + buses[0]

# from https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving
def find_timestamp_chinese_remainders_with_sieve(buses):
    # get largest modulus (bus number)
    bus_offset = {}
    for key, value in buses.items():
        bus_offset[value] = key
    # sort bus id's largest to smallest
    bus_ids = list(bus_offset.keys())
    bus_ids.sort()
    bus_ids.reverse()
    # start from earliest possible result (time of first bus)
    target = buses[0]
    step = 1
    for id in bus_ids:
        offset = bus_offset[id]
        while True:
            if (target + offset) % id == 0:
                step = step * id
                break                
            else:
                target = target + step        
    return target

if __name__ == '__main__':
    start_time, buses = read_timetable('input.txt')
    bus, wait_time = pick_bus(start_time, buses)
    part1 = bus * wait_time
    print(f'Part 1 - {part1}')
    buses = read_bus_positions('input.txt')
    part2 = find_timestamp_chinese_remainders_with_sieve(buses)
    print(f'Part 2 - {part2}')