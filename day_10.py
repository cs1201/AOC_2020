
def part_one(adaptors):
    diffs = []
    for i in range(len(adaptors)-1):
        diffs.append(adaptors[i+1] - adaptors[i])
    return diffs.count(1) * diffs.count(3)

def search_valid_chains(adaptors, valid_paths, i):
    if i == len(adaptors)-1: #At end of chain already
        return 1
    if i in valid_paths:
        return valid_paths[i] #Have already determined valid paths for this point
    num = 0
    for j in range(i+1, len(adaptors)): #Get possible path for rest of adaptors
        if (adaptors[j] - adaptors[i]) <= 3: # Check valid next adaptor
            num += search_valid_chains(adaptors, valid_paths, j) # Add to total and recursively get next path
    valid_paths[i] = num
    return num

def part_two(adaptors):
    valid_paths = {}
    return search_valid_chains(adaptors, valid_paths, 0)
        

with open("data/day_10.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]
    data.extend([0, max(data)+3])
    adaptors = sorted(data)
    print(f"Part One: {part_one(adaptors)}") #2812
    print(f"Part Two: {part_two(adaptors)}") #386869246296064