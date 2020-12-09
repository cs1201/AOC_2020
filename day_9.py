PREAMBLE_SIZE = 25

def check_valid(seq):
    val = seq[-1]
    preamble = seq[:-1]
    for a in preamble:
        for b in preamble:
            if a != b and a+b == val:
                return True
    return False

def part_one(data):
    for i, val in enumerate(data):
        if i > PREAMBLE_SIZE:
            if not check_valid(data[i-PREAMBLE_SIZE-1:i]):
                return data[i-1]


def part_two(data):
    invalid_val = part_one(data)
    for i, val_a in enumerate(data):
        running = []
        j = 1
        running.append(val_a)
        while sum(running) <= invalid_val:
            running.append(data[i+j])
            if sum(running) == invalid_val:
                return max(running) + min(running)
            j+=1

with open("data/day_9.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")

    assert(part_one(data) == 32321523)
    assert(part_two(data) == 4794981)