def count_valid_pws (pws:list, policies:list) -> int:
    


if __name__ == '__main__':
    # Read in the data
    with open('./day2_part1_input.txt', 'r') as f:
        part1_raw = f.readlines()

    # Format the data
    p1_policies = [policy_pw.split(':')[0] for policy_pw in part1_raw]
    p1_pws = [policy_pw.split(':')[1].lstrip(' ').rstrip('\n') for policy_pw in part1_raw]

    p1_mins = [policy.split(' ')[0].split('-')[0] for policy in p1_policies]
    p1_maxs = [policy.split(' ')[0].split('-')[1] for policy in p1_policies]
    p1_char = [policy[-1] for policy in p1_policies]

    