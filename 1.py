from src.Helper import Helper
from src.Event import Event
import sys


# Print header and challenge day
Helper.print_header(sys.argv[0].replace(".py", ""))

# Retrieve challenge input data
url = "https://adventofcode.com/2021/day/1/input"
data = Helper.retrieve_challenge_input(url, sys.argv[1])

# Solve challenge
Event("Solving challenge...")
previous = None
increased = 0
for sonar_reading in data:
    if sonar_reading != "":
        sonar_reading = int(sonar_reading)
    if previous != None and \
       sonar_reading != "" and \
       previous < sonar_reading:
        increased += 1
    previous = sonar_reading


# Print answer
Event("Challenge solved! Solution: " + str(result), is_success=True)
