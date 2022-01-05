"""
Day 5 Instructions: https://adventofcode.com/2021/day/5
"""
from icecream import ic
import numpy as np


# Part 1 ========================================================================
def draw_diagram(coordinates: list, diagram: np.array):
    x1, y1, x2, y2 = coordinates
    
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            diagram[x1, i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            diagram[i, y1] += 1

    return diagram


if __name__ == '__main__':
    with open('./05-12-2021_input.txt', 'r') as f:
        diag_keys = f.readlines()

    all_coords = [list(map(int, d.replace(' -> ', ',').split(','))) for d in diag_keys]
    largest_coord = np.array(all_coords).max()
    diagram = np.zeros((largest_coord + 1, largest_coord + 1))
    
    # Part 1 =====================================================================
    for coords in all_coords:
        draw_diagram(coords, diagram)

    num_overlapping_points = (diagram > 1).sum()
    ic(num_overlapping_points)
