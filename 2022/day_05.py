"""Advent of Code 2022 Day 5 Solution"""

from collections import defaultdict
import copy
from icecream import ic 


with open ('./day_05_input.txt', 'r', encoding='utf-8') as crates_n_procs:
    crates_n_procs_all = [cp.rstrip('\n') for cp in crates_n_procs.readlines()]

crates = crates_n_procs_all[:9]
procs = crates_n_procs_all[10:]


# Part 1 ===============================================
indices = [i for i in range(len(crates[-1])) if crates[-1][i].isnumeric()]
stack_by_ind = dict(zip(indices, range(1, 10)))

# Reverse the crates to create stacks (LIFO)
part1_stacks_by_ind = defaultdict(list)
crates = crates[::-1][1:]

for crate in crates:
    for i, ch in enumerate(crate):
        if i in stack_by_ind and ch != ' ':
            part1_stacks_by_ind[stack_by_ind.get(i)].append(ch)

part2_stacks_by_ind = copy.deepcopy(part1_stacks_by_ind)

for i, proc in enumerate(procs):
    proc = proc.split(' ')
    amount, fr, to = [int(p) for p in proc if p.isnumeric()]
    # part 1
    for _ in range(amount):
        last = part1_stacks_by_ind.get(fr).pop()
        part1_stacks_by_ind.get(to).append(last)

    top_amt = part2_stacks_by_ind.get(fr)[-amount:]
    part2_stacks_by_ind[fr]= part2_stacks_by_ind.get(fr)[: -amount]
    part2_stacks_by_ind.get(to).extend(top_amt) 

ic('Day 5: Part 1')
ic("After the rearrangement procedure completes, what crate ends up on top of each stack?")
crates_on_top_9000 = []
for stack_no, crates in part1_stacks_by_ind.items():
    crates_on_top_9000.append(crates[-1])
ic(''.join(crates_on_top_9000))


# Part 2 ===============================================
# Before the rearrangement process finishes,
# Update your simulation so that the Elves know where they should stand to be ready to unload the final supplies.
ic("Day 5: Part 2")
ic("After the rearrangement procedure completes, what crate ends up on top of each stack?")

ic(part2_stacks_by_ind)
# ic(stacks_by_ind_part2)
crates_on_top_9001 = []
for stk_no, cr in part2_stacks_by_ind.items():
    crates_on_top_9001.append(cr[-1])
ic(''.join(crates_on_top_9001))
