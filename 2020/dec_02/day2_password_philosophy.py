from collections import Counter

def count_valid_pws (pws:list, policies:list) -> int:
    assert len(pws) == len(policies)

    char_min = [int(policy.split(' ')[0].split('-')[0]) for policy in policies]
    char_max = [int(policy.split(' ')[0].split('-')[1]) for policy in policies]
    char = [policy[-1] for policy in p1_policies]

    counter = 0
    for i, pw in enumerate(pws):
        counts = Counter(pw)
        if counts.get(char[i]) and counts.get(char[i]) <= char_max[i] and counts.get(char[i]) >= char_min[i]:
            counter += 1
    
    return counter


if __name__ == '__main__':
    # Read in the data
    with open('./day2_part1_input.txt', 'r') as f:
        part1_raw = f.readlines()

    # Format the data
    p1_policies = [policy_pw.split(':')[0] for policy_pw in part1_raw]
    p1_pws = [policy_pw.split(':')[1].lstrip(' ').rstrip('\n') for policy_pw in part1_raw]

    # Part 1
    valid_pws = count_valid_pws(p1_pws, p1_policies)
    print(f'Valid Passwords: {valid_pws}')
    print()

    # Part 2
    
    