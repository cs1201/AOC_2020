import re

def validate_passport(passport):
    return all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def parse_passport(passport):
    raw_passport = re.split(' |\n', passport)

    # Convert passport to dict
    passport_dict = dict()
    for item in raw_passport:
        passport_dict[item.split(':')[0]] = item.split(':')[1]
    
    # Validate specific elements
    if validate_passport(passport):
        conditions = [  int(passport_dict['byr']) not in range(1920, 2003),
                        int(passport_dict['iyr']) not in range(2010, 2021),
                        int(passport_dict['eyr']) not in range(2020, 2031),
                        passport_dict['hcl'][0] != "#" or len(passport_dict['hcl']) != 7 or not passport_dict['hcl'][1:].isalnum(),
                        passport_dict['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                        len(passport_dict['pid']) != 9,
                        not all(x.isdigit() for x in passport_dict['pid']),
                        not any(passport_dict['hgt'][-2:] == measurement for measurement in  ["in", "cm"]),
                        passport_dict['hgt'][-2:] == "in" and int(passport_dict['hgt'][:-2]) not in range(59, 77),
                        passport_dict['hgt'][-2:] == "cm" and int(passport_dict['hgt'][:-2]) not in range(150, 194)]
        if any(conditions):
            return False
    else:
        return False
    return True

def part_one(data):
    return sum([validate_passport(passport) for passport in data])

def part_two(data):
    return sum([parse_passport(passport) for passport in data])

with open("data/day_4.txt") as f:
    data = [(x.strip()) for x in f.read().split("\n\n")]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")