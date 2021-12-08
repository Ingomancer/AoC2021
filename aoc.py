from diagnostic.binary import power_consumption
from dive.pilot import product_of_position
from hydrothermal.vents import count_overlaps
from lantern.fish import count_fish
from segment.search import parse_digits
from sonar.sweep import increasing_depths
import sys

from squid.bingo import find_winner
from whales.treachery import least_spent_fuel

daymap = {
    1: lambda x: increasing_depths(_input_as_int_list(x)),
    2: lambda x: product_of_position(_input_as_string_int_tuple_list(x)),
    3: lambda x: power_consumption(_input_as_string_list(x)),
    4: lambda x: find_winner(_input_as_string_list(x)),
    5: lambda x: count_overlaps(_input_as_string_list(x)),
    6: lambda x: count_fish(_input_as_int_list(x)),
    7: lambda x: least_spent_fuel(_input_as_int_list(x)),
    8: lambda x: parse_digits(_input_as_string_list(x)),
}

def main():
    if len(sys.argv) == 2:
        day = int(sys.argv[1])
    else:
        day = int(input("Pick day: "))
    with open(f"inputs/{day}", 'r') as input_file:
        print(daymap[day](input_file))

def _input_as_int_list(input_file):
    lines = input_file.readlines()
    if len(lines) > 1:
        return list(map(int, input_file.readlines()))
    else:
        return map(int, lines[0].split(','))

def _input_as_string_int_tuple_list(input_file):
    output = []
    for line in input_file.readlines():
        word, number = line.split()
        number = int(number)
        output.append((word, number))
    return output

def _input_as_string_list(input_file):
    return input_file.read().splitlines()

if __name__ == "__main__":
    main()