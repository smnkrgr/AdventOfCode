from src.Helper import Helper
from src.Event import Event

def clean_data(data):
    data = [entry.split(" ") \
            for entry in data if entry != ""]
    data = [[entry[0], int(entry[1])] for entry in data]
    return data

def calc_position(data):
    horizontal = 0
    depth = 0
    for entry in data:
        command = entry[0]
        val = entry[1]
        if command == "forward":
            horizontal += val
        elif command == "down":
            depth += val
        elif command == "up":
            depth -= val
    return horizontal, depth

def calc_position_extended(data):
    horizontal = 0
    depth = 0
    aim = 0
    for entry in data:
        command = entry[0]
        val = entry[1]
        if command == "forward":
            horizontal += val
            depth += aim * val
        elif command == "down":
            aim += val
        elif command == "up":
            aim -= val
    return horizontal, depth

if __name__=="__main__":
    # Retrieve challenge input data
    url = "https://adventofcode.com/2021/day/2/input"
    data = Helper.retrieve_challenge_input(url)
    data = clean_data(data)

    # Solve challenge
    Event("Solving challenge...")
    hor, depth = calc_position(data)
    c1_result = hor * depth
    hor, depth = calc_position_extended(data)
    c2_result = hor * depth

    # Print answer
    Event("Challenge 1 solved! Solution: " + \
            str(c1_result), is_success=True)
    Event("Challenge 2 solved! Solution: " + \
            str(c2_result), is_success=True)


