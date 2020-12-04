import re
from functools import reduce

def parse_file(filename):
    with open(filename) as f:
        current = {}
        entries = []
        for line in f.readlines():
            if len(line.strip()) == 0:
                entries.append(current)
                current = {}
            else:
                [add_part(current, entry) for entry in line.split(" ")]
        entries.append(current)
    return entries

def add_part(dict, part):
    kv = part.strip().split(":")
    dict[kv[0]] = kv[1]


def validate_num(num, min, max):
    try:
        value = int(num)
        return value >= min and value <= max
    except ValueError:
        return False


def validate_hgt(hgt):
    if hgt.endswith("cm"):
        return validate_num(hgt[0:-2], 150, 193)
    elif hgt.endswith("in"):
        return validate_num(hgt[0:-2], 59, 76)
    else:
        return False


def validate_byr(byr):
    return validate_num(byr, 1920, 2002)


def validate_iyr(iyr):
    return validate_num(iyr, 2010, 2020)


def validate_eyr(eyr):
    return validate_num(eyr, 2020, 2030)


def validate_hcl(hcl):
    return re.match('#[0-9a-f]{6}', hcl) is not None


def validate_ecl(ecl):
    return ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def validate_pid(pid):
    return re.match('[0-9]{9}', pid) is not None and len(pid) == 9


def valid_passport(passport):
    rules = {'byr': validate_byr,
             'iyr': validate_iyr,
             'eyr': validate_eyr,
             'hcl': validate_hcl,
             'hgt': validate_hgt,
             'ecl': validate_ecl,
             'pid': validate_pid}
    return reduce(lambda valid, key: valid and rules[key](passport[key]), rules, True)


def validate_passports(passports):
    return [passport for passport in passports if valid_passport(passport)]


def valid_fields_present(passport):
    validKeys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    missingKeys = [key for key in validKeys if key not in passport]
    return len(missingKeys) == 0


if __name__ == "__main__":
    passports = parse_file("input.txt")
    part1 = [
        passport for passport in passports if valid_fields_present(passport)]
    print(f"Part1 - {len(part1)}")
    part2 = validate_passports(passports)
    print(f"Part2 - {len(part2)}")
