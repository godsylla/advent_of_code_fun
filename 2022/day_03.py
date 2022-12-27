"""Solution for 2022 Day 3 Advent of Code"""
import string

from icecream import ic


# Part 1 =========================================
with open ("./day_03_input.txt", 'r', encoding='utf-8') as rs:
    rucksacks = [s.rstrip(' \n') for s in rs.readlines()]

priorities = dict(zip(string.ascii_letters, range(1, 53)))

priorities_of_items = []
for sack in rucksacks:
    midpoint = len(sack) // 2
    first_half = sack[: midpoint]
    second_half = sack[midpoint: ]
    assert len(first_half) == len(second_half)
    error = list(set(first_half).intersection(set(second_half)))[0]
    priorities_of_items.append(priorities.get(error))

ic("Part 1")
ic("Find the item type that appears in both compartments of each rucksack.")
ic("What is the sum of the priorities of those item types?")
ic(sum(priorities_of_items))


# Part 2 =========================================
# TODO
ic("Part 2")
ic("Find the item type that corresponds to the badges of each three-Elf group.")
ic("What is the sum of the priorities of those item types?") 
