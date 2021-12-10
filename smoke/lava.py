from collections import defaultdict
import math

def risk_levels(input):
    low_points = []
    basins = defaultdict(int)
    for coordinate, height in input.items():
        if _lowest_neighbour(coordinate, input)[0] > height:
            low_points.append(height)
        basin = _find_basin(coordinate, input)
        if basin:
            basins[basin] += 1
    return (sum(map(lambda x: x+1, low_points)), basins.pop(max(basins, key=basins.get))*basins.pop(max(basins, key=basins.get))*basins.pop(max(basins, key=basins.get)))


def _lowest_neighbour(coordinate, input):
    lowest = (math.inf, (-1, -1))
    for neighbour in _neighbours(coordinate, input):
        if input[neighbour] < lowest[0]:
            lowest = (input[neighbour], neighbour)
    return lowest

def _neighbours(coordinate, input):
    neighbours = []
    x, y = coordinate
    if (x-1, y) in input:
        neighbours.append((x-1, y))
    if (x+1, y) in input:
        neighbours.append((x+1, y))
    if (x, y-1) in input:
        neighbours.append((x, y-1))
    if (x, y+1) in input:
        neighbours.append((x, y+1))
    return neighbours

def _find_basin(coordinate, input):
    if input[coordinate] == 9:
        return None
    lowest_neighbour = _lowest_neighbour(coordinate, input)
    if lowest_neighbour[0] < input[coordinate]:
        return _find_basin(lowest_neighbour[1], input)
    return coordinate