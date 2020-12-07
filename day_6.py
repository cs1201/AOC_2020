# Get all unique reponses per group
def parse_reponses_1(response):
    return len(set(response))

# Get all consistent reponses between individuals in group
def parse_reponses_2(response):
    return len(set(response[0]).intersection(*response))
    
def part_one(data):
    return sum(parse_reponses_1(group) for group in data)

def part_two(data):
    return sum([parse_reponses_2(group) for group in data])

with open("data/day_6.txt") as f:
    # Data for part 1 is split by group. No need to know individuals responses within group
    data_1 = [[x for x in line if x != '\n'] for line in f.read().split('\n\n')]
    # Data for part 2 is split by group, then by individual
    f.seek(0)
    data_2 = [[[s for s in x] for x in line.split('\n')] for line in f.read().split('\n\n')]
    # print(data_2)
    print(f"Part One: {part_one(data_1)}")
    print(f"Part Two: {part_two(data_2)}")