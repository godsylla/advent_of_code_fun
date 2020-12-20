import numpy as np
from typing import List


def parse_input (raw_input_lines) : 
    fully_indexed_map = list()
    for line in raw_input_lines:
        fully_indexed_map.append(list(line))
    return np.array(fully_indexed_map)


def traverse_the_woods (woods:np.array, right:int=3, down:int=1):
    """
    count the number of trees ('#') encountered from top left to bottom right
    :woods: list of strings with characters '.' (no tree) and '#' (for tree)
    :right: numerator in slope
    :down: denominator in slope
    """
    total_rows, total_cols = woods.shape
    
    # start with 0th row, 0th column
    tree_count = 0 

    for r in range(0, total_rows, down):
        c = int((r * right / down) % total_cols)
        you_are_here = woods[r][c]
        if you_are_here == '#': tree_count += 1
        else: pass

    return tree_count


if __name__ == "__main__":
    with open ('./day3_part1_input.txt', 'r') as f1:
        part1_lines = f1.readlines()
    
    part1_rows = [line.rstrip('\n') for line in part1_lines]
    woods_1 = parse_input(part1_rows)
    trees_1 = traverse_the_woods(woods_1)
    print(trees_1)

