from collections import Counter


def parse_input (raw_input_lines:list) -> tuple:

    policies, passwords = [policy_pw.split(': ')[0] for policy_pw in raw_input_lines]
    chars = [policy[-1] for policy in policies]
    lower = [int(policy.split(' ')[0].split('-')[0]) for policy in policies]
    upper = [int(policy.split(' ')[0].split('-')[1]) for policy in policies]
    
    passwords = [policy_pw.split(': ')[1].rstrip('\n') for policy_pw in raw_input_lines]

    return lower, upper, chars, passwords


def count_valid_pws (raw_input_lines:list) -> int:
    mins, maxs, chars, pws = parse_input (raw_input_lines)

    counter = 0
    for i, pw in enumerate(pws):
        counts = Counter(pw)
        if counts.get(chars[i]) and counts.get(chars[i]) <= maxs[i] and counts.get(chars[i]) >= mins[i]:
            counter += 1
    
    return counter


def valid_char_locs (raw_input_lines:list) -> int:
    index_1, index_2, chars, pws = parse_input (raw_input_lines)

    counter = 0
    for i, pw in enumerate(pws):
        if chars[i] in pw:
            indices = [ind + 1 for ind, ltr in enumerate(pw) if ltr == chars[i]]
            if (index_1[i] in indices and index_2[i] not in indices) or (index_1[i] not in indices and index_2[i] in indices):
                counter += 1
    
    return counter


if __name__ == '__main__':
    # Read in the data
    with open('./day2_part1_input.txt', 'r') as f:
        part1_raw = f.readlines()
    
    with open('./day2_part2_input.txt', 'r') as f2:
        part2_raw = f2.readlines()
    
    # Part 1
    valid_pws1 = count_valid_pws(part1_raw)
    print(f'Valid Passwords: {valid_pws1}')
    print()

    # Part 2
    valid_pws2 = valid_char_locs(part2_raw)
    print(f'Revised Valid Passwords: {valid_pws2}')
    