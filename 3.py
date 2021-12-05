from src.Helper import Helper
from src.Event import Event

def clean_data(data):
    return [entry for entry in data if entry != ""]

def get_column(data, row_number):
    column = ""
    for entry in data:
        column += entry[row_number]
    return column

def get_most_common_char(string):
    char_dict = {}
    for char in string:
        if char not in char_dict.keys():
            char_dict[char] = 0
        else:
            char_dict[char] += 1
    return max(char_dict, key=char_dict.get)

def get_inverted(char):
    if char == "0":
        return "1"
    else:
        return "0"

def calc_rate(data, inverted=False):
    rate = ""
    for i in range(len(data[0])):
        column = get_column(data, i)
        if inverted:
            rate += get_inverted(get_most_common_char(column))
        else:
            rate += get_most_common_char(column)
    return int(rate, 2)

if __name__=="__main__":
    # Retrieve challenge input data
    url = "https://adventofcode.com/2021/day/3/input"
    data = Helper.retrieve_challenge_input(url)
    data = clean_data(data)

    # Solve challenge
    Event("Solving challenge...")
    gamma = calc_rate(data)
    epsilon = calc_rate(data, inverted=True)
    c1_result = gamma * epsilon

    # Print answer
    Event("Challenge 1 solved! Solution: " + \
            str(c1_result), is_success=True)
    Event("Challenge 2 solved! Solution: " + \
            str(""), is_success=True)


