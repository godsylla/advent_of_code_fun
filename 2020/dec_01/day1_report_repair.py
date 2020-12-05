

def find_pair_and_multiply(numbers: list, total: int=2020) -> float:

    pair = tuple()
    for num in numbers:
        diff = total - num
        if diff in numbers:
            pair = (num, diff)

    return pair


def find_triplet_and_multiply(numbers: list, total:int=2020) -> float:

    triplet = tuple()

    for num in numbers:
        diff_to_split = total - num
        try:
            subset = numbers.copy()
            subset.remove(num)
            if find_pair_and_multiply(subset, diff_to_split):find_pair_and_multiply(subset, diff_to_split)
                triplet = (num, )


        except:
            pass





if __name__ == '__main__':
    # Read in the input
    with open('./day1_input.txt', 'r') as f:
        txt_numbers = f.readlines()

    # Format the raw input
    numbers = [int(num.strip('\n')) for num in txt_numbers]

    p1_pair = find_pair_and_multiply(numbers)
    print(f'Part 1 answer: {p1_pair[0] * p1_pair[1]}')

    p2_triplet =



