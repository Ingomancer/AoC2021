import math

def increasing_depths(input):
    prev = math.inf
    count = 0
    sum_count = 0
    last_four = []
    for depth in input:
        last_four.append(depth)
        if len(last_four) == 4:
            prev_three = last_four[0] + last_four[1] + last_four[2]
            cur_three = last_four[1] + last_four[2] + last_four[3]
            del last_four[0]
            if cur_three > prev_three:
                sum_count += 1
        if depth > prev:
            count += 1
        prev = depth
    return (count, sum_count)
