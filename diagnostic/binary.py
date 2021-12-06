from collections import defaultdict


def power_consumption(input):
    gamma = ""
    epsilon = ""
    count_per_pos = _count_per_pos(input)
    for pos in count_per_pos:
        zeroes, ones = _zeroes_and_ones(count_per_pos, pos)
        if ones > zeroes:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    
    oxygen_rating = _determine_rating(input, 0, _oxygen_criteria)
    co2_rating = _determine_rating(input, 0, _co2_criteria)
    return (int(gamma, 2) * int(epsilon, 2), int(oxygen_rating, 2) * int(co2_rating, 2))

def _determine_rating(potentials, pos, bit_criteria):
    if len(potentials) == 1:
        return potentials[0]
    count_per_pos = _count_per_pos(potentials)
    zeroes, ones = _zeroes_and_ones(count_per_pos, pos)
    bit_to_keep = bit_criteria(zeroes, ones)
    potentials = list(filter(lambda x: x[pos] == bit_to_keep, potentials))
    pos += 1
    return _determine_rating(potentials, pos, bit_criteria)   

    
def _count_per_pos(input):
    count_per_pos = defaultdict(lambda: defaultdict(int))
    for line in input:
        for idx, bit in enumerate(line):
            count_per_pos[idx][bit] += 1
    return count_per_pos

def _zeroes_and_ones(count_per_pos, pos):
    zeroes = count_per_pos[pos]['0']
    ones = count_per_pos[pos]['1']
    return (zeroes, ones)

def _oxygen_criteria(zeroes, ones):
    if zeroes > ones:
        bit_to_keep = "0"
    else:
        bit_to_keep = "1"
    return bit_to_keep

def _co2_criteria(zeroes, ones):
    if ones < zeroes:
        bit_to_keep = "1"
    else:
        bit_to_keep = "0"
    return bit_to_keep