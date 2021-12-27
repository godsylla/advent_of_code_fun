"""
Part 1 directions: https://adventofcode.com/2021/day/2#part1 
Part 2 directions: https://adventofcode.com/2021/day/2#part2
"""
from icecream import ic 

def calc_net_position (vectors: list):
    """
    :vectors: have a direction, and a magnitude
        list of lists
        first position of ea child list is direction
        second position of ea child list is magnitude
    """
    net_vertical = 0
    net_horizontal = 0

    dir = [v[0] for v in vectors]
    mag = [int(v[1]) for v in vectors]

    for d, m in zip(dir, mag):
        if d == 'forward':
            net_horizontal += m
        elif d == 'up':
            net_vertical -= m
        else: 
            net_vertical += m

    return net_horizontal, net_vertical

    
if __name__ == '__main__':

    # Input
    with open('./02-12-2021_input.txt', 'r') as f:
        parsed_lines = f.readlines()
    dir_amts = [pl.rstrip('\n').split(' ') for pl in parsed_lines]
    
    # Part 1 
    net_horiz, net_vert = calc_net_position(dir_amts)
    ic(net_horiz * net_vert)


