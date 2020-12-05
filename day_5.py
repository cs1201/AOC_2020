import math
NUM_ROWS = 128
NUM_COLUMNS = 8

def bsp(sector, valid_range):
    if sector == "F" or sector == "L":
        valid_range = valid_range[:round(len(valid_range)/2)]
    if sector == "B" or sector == "R":
        valid_range = valid_range[round(len(valid_range)/2):] 
    return valid_range

def calculate_seat_id(r, c):
    return r * 8 + c

def find_seat_id(seat_map, seat_id):
    return any(seat_id in row for row in seat_map)

def get_seat_info(boarding_number):
    row_info, column_info = boarding_number[:-3], boarding_number[-3:]
    valid_row_range, valid_column_range = range(0, NUM_ROWS), range(0, NUM_COLUMNS)
    # ROW
    for i, sector in enumerate(row_info):
        valid_row_range = bsp(row_info[i], valid_row_range)
        if valid_row_range[0] == valid_row_range[-1]:
            row = valid_row_range[0]
    # COLUMN
    for i, sector in enumerate(column_info):
        valid_column_range = bsp(column_info[i], valid_column_range)
        if valid_column_range[0] == valid_column_range[-1]:
            column = valid_column_range[0]

    return row, column, calculate_seat_id(row, column)


def part_one(data):
    return max([get_seat_info(boarding_pass)[2] for boarding_pass in data])


def part_two(data):
    # Create seat map
    seat_map = [[0]* NUM_COLUMNS for _ in range(NUM_ROWS)]
    for boarding_pass in data:
        row, column, seat_id = get_seat_info(boarding_pass)
        seat_map[row][column] = seat_id
    # Extract empty seats
    empty_seats = []
    for x, row in enumerate(seat_map):
        for y, seat_id in enumerate(row):
            if seat_id == 0:
                empty_seats.append((x,y))
    # Find empty seat with valid neigbouring seat_ids
    for r, c in empty_seats:
        seat_id = calculate_seat_id(r, c)
        if find_seat_id(seat_map, seat_id+1) and find_seat_id(seat_map, seat_id-1):
            return(seat_id)


with open("data/day_5.txt") as f:
    data = [x.strip() for x in f.readlines()]
    print(f"Part One: {part_one(data)}")
    print(f"Part Two: {part_two(data)}")