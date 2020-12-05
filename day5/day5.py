from functools import reduce

def get_seat(ticket):
    col,row = reduce(find_range, ticket, ((0, 7), (0, 127)))
    return (col[0], row[0])

def find_range(xs_and_ys, char):
    (xmin, xmax), (ymin, ymax) = xs_and_ys
    if char == 'F':
        return ((xmin, xmax), (ymin, ymin+(ymax-ymin-1)/2))
    elif char == 'B':
        return ((xmin, xmax), (ymax - (ymax-ymin-1)/2, ymax))
    elif char == 'L':
        return ((xmin, xmin + (xmax-xmin-1)/2), (ymin, ymax))
    elif char == 'R':
        return ((xmax - (xmax-xmin-1)/2, xmax), (ymin, ymax))

def read_seats(file):
    with open(file) as f:
        return [get_seat(line.strip()) for line in f.readlines()]

def get_seat_id(seat):
    col, row = seat
    return col + row*8

def get_missing_seat(seat_ids):
    curr_seat_id = 0
    for seat_id in seat_ids:
        if curr_seat_id+2==seat_id:
            return seat_id - 1
        curr_seat_id = seat_id

def get_seat_ids(file):
    seats = read_seats(file)
    seat_ids = [get_seat_id(seat) for seat in seats]
    seat_ids.sort()
    return seat_ids

seat_ids = get_seat_ids("input.txt")
part1 = max(seat_ids)
print(f"Part1 - {part1}")
part2 = get_missing_seat(seat_ids)
print(f"Part2 - {part2}")