from dive.pilot import product_of_position
from sonar.sweep import increasing_depths
import sys

daymap = {
    1: lambda x: increasing_depths(_input_as_ints(x)),
    2: lambda x: product_of_position(_input_as_string_int_tuple(x)),
}

def main():
    if len(sys.argv) == 2:
        day = int(sys.argv[1])
    else:
        day = int(input("Pick day: "))
    with open(f"inputs/{day}", 'r') as input_file:
        print(daymap[day](input_file))

def _input_as_ints(input_file):
    return map(int, input_file.readlines())

def _input_as_string_int_tuple(input_file):
    output = []
    for line in input_file.readlines():
        word, number = line.split()
        number = int(number)
        output.append((word, number))
    return output

if __name__ == "__main__":
    main()