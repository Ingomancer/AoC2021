from collections import defaultdict
import timeit

def count_fish(input):
    count_of_fish = defaultdict(int)
    sum_80 = 0
    for fish in input:
        count_of_fish[fish] += 1
    for i in range(100000):
        if i == 80:
            sum_80 = sum(count_of_fish.values()) 
        new_count_of_fish = defaultdict(int)
        for key, value in count_of_fish.items():
            if key == 0:
                new_count_of_fish[8] = value
                new_count_of_fish[6] += value
            else:
                new_count_of_fish[key-1] += value
        count_of_fish = new_count_of_fish
    return (sum_80, sum(count_of_fish.values()))

# I wrote this faster version just to see how wasteful it is to create a temporary dict. The above version took 2.3 seconds for 100k days, this one 0.3
# For one million days, the above took several minutes, and this took 22 seconds. However, I missed assigning to an index like three times writing it
# so I definitely prefer the above solution
def count_fish_faster(input):
    count_of_fish = defaultdict(int)
    sum_80 = 0
    for fish in input:
        count_of_fish[fish] += 1
    for i in range(100000):
        if i == 80:
            sum_80 = sum(count_of_fish.values()) 
        new_6 = count_of_fish[0] + count_of_fish[7]
        count_of_fish[7] = count_of_fish[8]
        count_of_fish[8] = count_of_fish[0]
        count_of_fish[0] = count_of_fish[1]
        count_of_fish[1] = count_of_fish[2]
        count_of_fish[2] = count_of_fish[3]
        count_of_fish[3] = count_of_fish[4]
        count_of_fish[4] = count_of_fish[5]
        count_of_fish[5] = count_of_fish[6]
        count_of_fish[6] = new_6
    return (sum_80, sum(count_of_fish.values()))