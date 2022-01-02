"""
Part 1 directions: https://adventofcode.com/2021/day/2#part1 
Part 2 directions: https://adventofcode.com/2021/day/2#part2
"""
from icecream import ic 

def calc_net_position (directions: list, magnitudes: list):
    """
    :vectors: have a direction, and a magnitude
        list of lists
        first position of ea child list is direction
        second position of ea child list is magnitude
    """
    net_vertical = 0
    net_horizontal = 0

    for d, m in zip(directions, magnitudes):
        if d == 'forward':
            net_horizontal += m
        elif d == 'up':
            net_vertical -= m
        else: 
            net_vertical += m

    return net_horizontal, net_vertical


def calc_net_position_w_aim (directions: list, magnitudes: list):
    net_vertical = 0
    net_horizontal = 0
    net_aim = 0

    for d, m in zip(directions, magnitudes):
        if d == 'down':
            net_aim += m
            # net_vertical += m
        elif d == 'up':
            net_aim -= m
            # net_vertical -= m
        elif d == 'forward':
            net_horizontal += m
            net_vertical += (net_aim * m)
        
    return net_horizontal, net_vertical

    
if __name__ == '__main__':

    # Input
    with open('./02-12-2021_input.txt', 'r') as f:
        parsed_lines = f.readlines()
    dir_amts = [pl.rstrip('\n').split(' ') for pl in parsed_lines]
    dir = [v[0] for v in dir_amts]
    mag = [int(v[1]) for v in dir_amts]
    
    # Part 1 
    net_horiz, net_vert = calc_net_position(dir, mag)
    ic(net_horiz * net_vert)

    # Part 2
    net_horiz, net_vert = calc_net_position_w_aim(dir, mag)
    ic(net_horiz * net_vert)
