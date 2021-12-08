from collections import defaultdict

def parse_digits(input):
    easy_sum = 0
    hard_sum = 0
    for line in input:
        uniques, output = line.split(' | ')

        easy_sum += _count_easy_digits(output)

        hard_sum += _count_all_digits(uniques, output)

    return (easy_sum, hard_sum)

def _count_all_digits(uniques, output):
    digits_by_length = defaultdict(list)
    segment_letters = {}
    wires_for_number = {}
        
    for digit in uniques.split():
        digits_by_length[len(digit)].append(set(digit))
    wires_for_number = _solve_givens(digits_by_length, wires_for_number)
    segment_letters['a'] = wires_for_number[7] - wires_for_number[1]
    wires_for_number = _solve_six_segments(digits_by_length, segment_letters, wires_for_number)
    wires_for_number = _solve_five_segments(digits_by_length, wires_for_number)

    output_digits = ""
    for letters in output.split():
        for key, value in wires_for_number.items():
            if value == set(letters):
                output_digits += str(key)
    return int(output_digits)

def _solve_five_segments(digits_by_length, wires_for_number):
    for digit in digits_by_length[5]:
        if len(digit - wires_for_number[1]) == 3:
            wires_for_number[3] = digit
        elif len(digit - wires_for_number[4]) == 3:
            wires_for_number[2] = digit
        else:
            wires_for_number[5] = digit
    return wires_for_number

def _solve_six_segments(digits_by_length, segment_letters, wires_for_number):
    for digit in digits_by_length[6]:
        if len(digit - wires_for_number[4] - segment_letters['a']) == 1:
            wires_for_number[9] = digit
        elif len(digit - wires_for_number[1]) == 4:
            wires_for_number[0] = digit
        elif len(digit - wires_for_number[1]) == 5:
            wires_for_number[6] = digit
    return wires_for_number

def _solve_givens(digits_by_length, wires_for_number):
    wires_for_number[1] = digits_by_length[2][0]
    wires_for_number[7] = digits_by_length[3][0]
    wires_for_number[4] = digits_by_length[4][0]
    wires_for_number[8] = digits_by_length[7][0]
    return wires_for_number

def _count_easy_digits(output):
    one = four = seven = eight = 0
    for digit in output.split():
        if len(digit) == 2:
            one += 1
        elif len(digit) == 3:
            seven += 1
        elif len(digit) == 4:
            four += 1
        elif len(digit) == 7:
            eight += 1
    return one + four + seven + eight