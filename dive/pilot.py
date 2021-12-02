def product_of_position(input):
    hor_pos = 0
    depth_with_aim = 0
    depth = 0
    aim = 0
    for direction, distance in input:
        if direction == "forward":
            hor_pos += distance
            depth_with_aim += aim*distance
        elif direction == "down":
            depth += distance
            aim += distance
        elif direction == "up":
            depth -= distance
            aim -= distance
        else:
            raise ValueError
    return (hor_pos * depth, hor_pos * depth_with_aim)