def least_spent_fuel(input):
    input = list(input)
    part_1 = min(map(lambda target: sum(map(lambda element: abs(element-target), input)), range(min(input), max(input))))
    part_2 = min(map(lambda target: sum(map(lambda element: _triangular(abs(element-target)), input)), range(min(input), max(input))))
    return (part_1, part_2)

def _triangular(n):
    return (n*(n+1))/2