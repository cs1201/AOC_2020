
SUM_TARGET = 2020

#PART 1
def part_one(data):
    for num_a in data:
        if SUM_TARGET - num_a in data:
            return (SUM_TARGET - num_a) * num_a 

#PART 2
def part_two(data):
    for num_a in data:
        for num_b in data:
            if (SUM_TARGET - num_a - num_b) in data:
                return num_a * num_b * (SUM_TARGET - num_a - num_b)


with open("data/day_1.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")