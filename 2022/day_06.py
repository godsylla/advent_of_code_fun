"""Day 6 Advent of Code 2022 Solution"""

from icecream import ic

# Part 1 ==================================================
with open('./day_06_input.txt', 'r', encoding='utf-8') as sr:
    subroutine = sr.readline()

ic("Day 6, Part 1:")
ic("How many characters need to be processed before the first start-of-packet marker is detected?")
for i in range(len(subroutine) - 4):
    window = subroutine[i: i+4]
    if len(set(window)) == len(window):
        ic(i + 4)
        ic(window)
        break


# Part 2 ==================================================
ic("Day 6, Part 2:")
ic("How many characters need to be processed before the first start-of-packet marker is detected?")

for i in range(len(subroutine) - 14):
    window = subroutine[i: i + 14]
    if len(set(window)) == len(window):
        ic(i + 14)
        ic(window)
        break