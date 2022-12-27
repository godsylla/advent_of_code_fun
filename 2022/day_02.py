"""Solution for 2022 Day 1 Advent of Code"""

from icecream import ic


# Read input
with open("./day_02_input.txt", "r", encoding="utf-8") as d2i:
    tournament_rounds = d2i.readlines()

# Part 1 =========================================
# X for Rock, Y for Paper, and Z for Scissors
my_choice = dict(X="Rock", Y="Paper", Z="Scissors")
scoring = dict(Rock=1, Paper=2, Scissors=3)

win_loss = dict(AX=3, AY=6, AZ=0, BX=0, BY=3, BZ=6, CX=6, CY=0, CZ=3)

# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).
round_score = []

for rps_round in tournament_rounds:
    opp_ch, my_ch = rps_round.rstrip("\n").split(" ")
    win_loss_score = win_loss.get(opp_ch + my_ch)
    round_score.append(win_loss_score + scoring.get(my_choice.get(my_ch)))

# What would your total score be if everything goes exactly according to your strategy guide?
ic("Part 1: What is my score if I follow strategy guide?")
ic(sum(round_score))


# Part 2 =========================================
# the second column says how the round needs to end:
# X means you need to lose,
# Y means you need to end the round in a draw, and
# Z means you need to win
exp_ending = dict(X=0, Y=3, Z=6)

# A for Rock, B for Paper, and C for Scissors.
opponent_choice = dict(A="Rock", B="Paper", C="Scissors")

# Reverse Eng choice:
rev_eng = dict()
for combo, wl_score in win_loss.items():
    if wl_score in rev_eng:
        rev_eng[wl_score].append(combo)
    else:
        rev_eng[wl_score] = [combo]

part_2_score = []
for rps_round in tournament_rounds:
    opp_ch, wl_outcome = rps_round.rstrip("\n").split(" ")
    my_ch = [
        ch[1] for ch in rev_eng.get(exp_ending.get(wl_outcome)) if ch[0] == opp_ch
    ][0]
    part_2_score.append(exp_ending.get(wl_outcome) + scoring.get(my_choice.get(my_ch)))

ic("Part 2: What is my score if I follow strategy guide?")
ic(sum(part_2_score))
