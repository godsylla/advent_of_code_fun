"""
Day 3 Part 1 Directions: https://adventofcode.com/2021/day/3
Day 3 Part 2 Directions: https://adventofcode.com/2021/day/3#part2
"""
from collections import Counter
from icecream import ic 


# Part 1
def convert_binary_to_decimal (binary: str):
    reversed = binary[::-1]
    numerator = 0
    for i, r in enumerate(reversed): 
        if r != '0':
            numerator += 2 ** i
    return numerator 

def find_gamma_and_epsilon (binaries: list):
    unif_length = len(binaries[0])
    gamma = ''
    epsilon = ''

    for i in range(unif_length):
        counts = list(Counter([b[i] for b in binaries]).most_common())
        gamma += counts[0][0]
        epsilon += counts[1][0]
    return gamma, epsilon


# Part 2
def find_rating(binaries: list, rating_type: str):
    bin_length = len(binaries[0])
    scrubbed = binaries
    rating = None

    for i in range(bin_length):
        counts = list(Counter([s[i] for s in scrubbed]).most_common())
        if len(counts) > 1: 
            if rating_type == 'o2':
                if counts[0][1] == counts[1][1]:
                    filter_on = '1'
                else:
                    filter_on = counts[0][0]
            else:
                if counts[0][1] == counts[1][1]:
                    filter_on = '0'
                else:
                    filter_on = counts[1][0]
        
        # update the scrub based on update filter criteria
        scrubbed = [s for s in scrubbed if s[i] == filter_on]
        if len(scrubbed) != 0:
            rating = convert_binary_to_decimal(scrubbed[0])
        else: 
            break
    
    return rating


if __name__ == '__main__':

    # Input
    with open('./03-12-2021_input.txt', 'r') as f:
        parsed_lines = f.readlines()
    binaries = [l.strip('\n') for l in parsed_lines]

    # Part 1
    gamma, epsilon = find_gamma_and_epsilon(binaries)
    gamma_rate = convert_binary_to_decimal(gamma)
    epsilon_rate = convert_binary_to_decimal(epsilon)

    ic(gamma, epsilon)
    ic(gamma_rate)
    ic(epsilon_rate)
    ic(gamma_rate * epsilon_rate)

    # Part 2
    print('\n')
    o2_rating = find_rating(binaries, 'o2')
    co2_rating = find_rating(binaries, 'co2')
    ic(o2_rating)
    ic(co2_rating)
    ic(o2_rating * co2_rating)
    