from collections import Counter

def find_any_yes_per_group (input:list) -> int:
    group_answers = list()
    unique_answers = set()

    for line in raw_input:
        if line != '':
            unique_answers.update(set(line))
        else:
            group_answers.append(len(unique_answers))
            unique_answers = set()

    return sum(group_answers)


def find_all_yes_per_group (groups:list) -> int:
    """
    groups : list where each element is a list of passengers in that group
    """
    group_samesies = list()

    for g in groups:
        num_passengers = len(g)

        same_answers = Counter()
        for answers in g:
            same_answers.update(Counter(answers))
        
        answer_counts = same_answers.most_common()
        group_samesies.append(len([ans[0] for ans in answer_counts if ans[1] == num_passengers]))

    return sum(group_samesies)


if __name__ == '__main__':
    with open ('./day6_part1_input.txt') as f: 
        raw_input = [elem.strip() for elem in f.readlines()]
    raw_input += ['']

    # Part 1
    print('Part 1:')
    print(find_any_yes_per_group (raw_input), '\n')

    # Part 2
    # Form separate groups
    groups = list()
    g = list()
    for line in raw_input: 
        if line != '':
            g.append(line)
        else:
            groups.append(g)
            g = list()

    print('Part 2:')
    print(find_all_yes_per_group(groups))

