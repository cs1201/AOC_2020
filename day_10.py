
def part_one(data):
    available = sorted(data.copy())
    available.append(max(available)+3)
    available.insert(0, 0)
    diffs = []
    for i in range(len(available)-1):
        diffs.append(available[i+1] - available[i])
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

def part_two(data):
    valid_paths = {}
    adaptors = []
    adaptors.append(0)
    adaptors.extend(sorted(data))
    adaptors.append(max(adaptors)+3)
    return search_valid_chains(adaptors, valid_paths, 0)
        

with open("data/day_10.txt") as f:
    data = [int(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}") #2812
    print(f"Part Two: {part_two(data)}") #386869246296064