with open ('./day6_part1_input.txt') as f: 
    raw_input = [elem.strip() for elem in f.readlines()]

raw_input += ['']

group_answers = list()
unique_answers = set()

for line in raw_input:
    if line != '':
        unique_answers.update(set(line))
    else:
        group_answers.append(len(unique_answers))
        unique_answers = set()

print(sum(group_answers))