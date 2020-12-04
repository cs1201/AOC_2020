

def validate_passport(passport):
    return all(key in passport for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])

def part_one(data):
    return sum([validate_passport(passport) for passport in data])

def part_two(data):
    ...

with open("data/day_4.txt") as f:
    data = [(x.strip()) for x in f.read().split("\n\n")]
    # print(data)
    print(f"Part One: {part_one(data)}")
    # print(f"Part Two: {part_two(data)}")