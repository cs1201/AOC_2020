
Tree = True
Open = False

def parse_map(data):
    route_map = []
    for line in data:
        route_map.append([(Tree if square == "#" else Open) for square in line])
    return route_map

def traverse_map(data, rule):
    route_map = parse_map(data)
    y_len = len(route_map)
    x_len = len(route_map[0])
    x,y,tree_sum = 0,0,0

    while True:
        # Traverse x right, y down
        x += rule[0]
        y += rule[1]

        # If still in y bounds, check cell at route x across, y down to see if there's a tree
        if y < y_len:
            if route_map[y][x % x_len]:
                tree_sum += 1
        else:
            break
    return tree_sum

def part_one(data):
    return traverse_map(data, (3,1))
    
def part_two(data):
    routes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    tree_product = 1
    for route in routes:
        tree_product *= traverse_map(data, route)
    return tree_product

with open("data/day_3.txt") as f:
    data = [(x.strip()) for x in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")
    assert part_one(data) == 299
    assert part_two(data) == 3621285278