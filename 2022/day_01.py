"""Solution for 2022 Day 1 Advent of Code"""

from icecream import ic


# Part 1 Solution ================================================
# Find the Elf carrying the most Calories. 
# How many total Calories is that Elf carrying?

with open ('./day_01_input.txt', 'r', encoding='utf-8') as ipt:
    # reads in as list of strings
    parsed_lines = ipt.readlines()

calories = []
running_sum = 0
for line in parsed_lines:
    if line != '\n':
        running_sum += int(line)
    else:
        calories.append(running_sum)
        running_sum = 0

print("Part 1: Max Number of Calories")
ic(max(calories))


# Part 2 Solution ================================================
# Find the top three Elves carrying the most Calories.
# How many Calories are those Elves carrying in total?
print("Part 2: Sum of Calories carried by Top 3 Elves")

rev_calories = sorted(calories, reverse=True)
ic(sum(rev_calories[:3]))
