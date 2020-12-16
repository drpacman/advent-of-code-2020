import re 

def parse_input(file):
    valid_values = {}
    ticket = []
    nearby = []
    with open(file) as f:
        section=1
        lines = [ line.strip() for line in f.readlines() ]
        for line in lines:
            if line == 'your ticket:':
                section = 2
                continue
            elif line == 'nearby tickets:':
                section = 3
                continue
            elif section == 1:
                matches = re.match("([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
                if matches != None:
                    valid_values[matches[1]] = list(range(int(matches[2]), int(matches[3])+1)) + list(range(int(matches[4]), int(matches[5])+1))            
            elif section == 2 and line != '':
                ticket = [ int(val) for val in line.split(',') if val != '' ]
            elif section == 3 and line != '':
                nearby.append([ int(val) for val in line.split(',') if val != '' ])
    return (valid_values, ticket, nearby)

class TicketOffice():
    def __init__(self, values):
        self.values = values

    def is_valid_value(self,value):
        for _, values in self.values.items():
            if value in values:
                return True
        return False
            
    def invalid_values(self, ticket):
        return list(filter(lambda x: self.is_valid_value(x) == False, ticket))
    
    def is_valid_ticket(self, ticket):
        return all([ self.is_valid_value(value) for value in ticket ])
    
    def is_valid_position(self, key, pos, tickets):
        return all( [ ticket[pos] in self.values[key] for ticket in tickets] )
            
    def remove_options(self, possibilities):
        for key, p in possibilities.items():
            if len(p) == 1:
                value = p[0]
                for key2, p2 in possibilities.items():
                    if key2 == key:
                        continue
                    if value in p2:
                        p2.remove(value)
                        return self.remove_options(possibilities)
        return possibilities

    def resolve_fields(self, tickets):
        valid_tickets = list(filter(self.is_valid_ticket, tickets))
        field_count = len(self.values)
        possible_positions = {}
        for key in self.values.keys():
            possible_positions[key] = [ pos for pos in range(field_count) if self.is_valid_position(key, pos, valid_tickets) ]
        
        cleaned = self.remove_options(possible_positions)        
        return { key : cleaned[key][0] for key in cleaned.keys() }

valid_values, ticket, nearby = parse_input('input.txt')
t = TicketOffice(valid_values)
invalid_items = ([ t.invalid_values(item) for item in nearby])
part1 = (sum([item for items in invalid_items for item in items]))
print(f"Part 1 - {part1}")
all_tickets = nearby.copy()
all_tickets.append(ticket)
values = t.resolve_fields( all_tickets )
part2 = 1
for key, value in values.items():
    if key.startswith('departure'):
        part2 = part2 * ticket[value]
print(f"Part 2 - {part2}")



