from typing import Match
from sonar.sweep import increasing_depths
import sys

def main():
    if len(sys.argv) == 2:
        day = int(sys.argv[1])
    else:
        day = int(input("Pick day: "))
    if day == 1:
        with open("sonar/input", 'r') as input_file:
            print(increasing_depths(map(int, input_file.readlines())))
    

if __name__ == "__main__":
    main()