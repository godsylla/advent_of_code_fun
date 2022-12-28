"""Solution for 2022 Day 4 Advent of Code"""

from icecream import ic

with open ('./day_04_input.txt', 'r', encoding='utf-8') as p:
    pairs = [prs.rstrip(' \n').split(',') for prs in p.readlines()]    

ic("Day 4: Part 1")
ic("In how many assignment pairs does one range fully contain the other?")

FULLY_CONTAINED_PAIRS = 0
OVERLAPPING_PAIRS = 0
for i, pair in enumerate(pairs):
    first, second = pair
    f_lower, f_upper = list(map(int, first.split('-')))
    s_lower, s_upper = list(map(int, second.split('-')))

    # check first contains second
    if (f_lower >= s_lower) and (f_upper <= s_upper):
        FULLY_CONTAINED_PAIRS += 1

    # check second contains first
    elif (s_lower >= f_lower) and (s_upper <= f_upper):
        FULLY_CONTAINED_PAIRS += 1

    elif any(i in range(f_lower, f_upper + 1) for i in range(s_lower, s_upper + 1)):
        OVERLAPPING_PAIRS += 1

    else:
        pass

ic(FULLY_CONTAINED_PAIRS)

ic("Day 4: Part 2 ")
ic("In how many assignment pairs do the ranges overlap?")
ic(OVERLAPPING_PAIRS + FULLY_CONTAINED_PAIRS)
