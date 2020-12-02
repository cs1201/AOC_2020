from collections import Counter

def parse_password(entry):
    frequency = entry.split()[0]
    letter = entry.split()[1].split(":")[0]
    password = entry.split()[2]
    min_freq, max_freq = [int(i) for i in frequency.split('-')]

    return password, letter, min_freq, max_freq

def validate_password_a(entry):

    password, letter, min_freq, max_freq = parse_password(entry)
    appearances = Counter(password)
    if letter not in appearances.keys():
        return False

    freq = int(appearances[letter])
    if freq not in range(min_freq, max_freq+1):
        return False

    return True

def validate_password_b(entry):
    # Valid if pos_a XOR pos_b of password == letter
    password, letter, pos_a, pos_b = parse_password(entry)
    return (password[pos_a - 1] == letter) ^ (password[pos_b - 1] == letter)

def part_one(data):
    return sum([validate_password_a(entry) for entry in data])

def part_two(data):
    return sum([validate_password_b(entry) for entry in data])

with open("data/day_2.txt") as f:
    data = [x.strip() for x in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")