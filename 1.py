from src.Helper import Helper
from src.Event import Event

def clean_data(data):
    return [int(entry) for entry in data if entry != ""]

def calc_increased_readings(data):
    previous = None
    increased = 0
    for sonar_reading in data:
        if previous != None and \
           previous < sonar_reading:
            increased += 1
        previous = sonar_reading
    return increased

def calc_sliding_window(data, window=3):
    data_sliding = []
    for i in range(len(data)-window+1):
        sliding_val = 0
        for x in range(window):
            sliding_val += data[i+x]
        data_sliding.append(sliding_val)
    return data_sliding

if __name__=="__main__":
    # Retrieve challenge input data
    url = "https://adventofcode.com/2021/day/1/input"
    data = Helper.retrieve_challenge_input(url)
    data = clean_data(data)

    # Solve challenge
    Event("Solving challenge...")
    c1_increased = calc_increased_readings(data)
    sliding = calc_sliding_window(data)
    c2_increased = calc_increased_readings(sliding)

    # Print answer
    Event("Challenge 1 solved! Solution: " + \
            str(c1_increased), is_success=True)
    Event("Challenge 2 solved! Solution: " + \
            str(c2_increased), is_success=True)


