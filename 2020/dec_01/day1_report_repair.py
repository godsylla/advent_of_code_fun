

def find_pair (numbers: list, total: int=2020) -> float:

    pair = tuple()
    for num in numbers:
        diff = total - num
        if diff in numbers:
            pair = (num, diff)

    return pair


def find_triplet (numbers: list, total:int=2020) -> float:

    triplet = tuple()

    for num in numbers:
        diff_to_split = total - num

        try:
            subset = numbers.copy()
            subset.remove(num)
            pair = find_pair (subset, diff_to_split)
            
            if len(pair) != 0:
                triplet = (num, pair[0], pair[1])
            
        except:
            pass

    return triplet


if __name__ == '__main__':
    # Read in the input
    with open('./day1_part1_input.txt', 'r') as f:
        pt1_txt_numbers = f.readlines()
    with open('./day1_part2_input.txt', 'r') as f:
        pt2_txt_numbers = f.readlines()

    # Format the raw input
    numbers_1 = [int(num.strip('\n')) for num in pt1_txt_numbers]
    numbers_2 = [int(num.strip('\n')) for num in pt2_txt_numbers]

    p1_pair = find_pair (numbers_1)
    print(p1_pair)
    print(f'Part 1 answer: {p1_pair[0] * p1_pair[1]}')

    print()
    p2_triplet = find_triplet(numbers_2)
    print(p2_triplet)
    print(f"Part 2 answer: {p2_triplet[0] * p2_triplet[1] * p2_triplet[2]}")



