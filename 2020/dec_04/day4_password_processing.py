"""
Validate if a given passport is a valid passport
"""
from collections import Counter
import random
from typing import List

from pprint import pprint


def parse_passports (passport_filepath:str) -> List[dict]:
    with open (passport_filepath, 'r') as f:
        raw_input = [entry.strip() for entry in f.readlines()]

    all_passports = []
    count = 0

    for line in raw_input:

        all_passports.append(dict())

        if line != "":
            data = [_.split(":") for _ in line.split()]
            for elem in data:
                all_passports[count].update({elem[0] : elem[1]})
        else:
            count += 1

    return list(filter(None, all_passports))


def check_passport_validity (passport:dict) -> bool:
    """
    if all valid fields present --> valid
    if only cid is missing --> valid, otherwise invalid
    if cid + other field missing --> invalid
    """
    return len(passport) == 8 or len(passport) == 7 and 'cid' not in passport


if __name__ == '__main__':
    all_passports = parse_passports('./day4_part1_input.txt')
    print(f'{len(all_passports)} in total.')

    valid_count = []

    for passport in all_passports:
        valid_count.append(check_passport_validity(passport))
        
    print(Counter(valid_count)[True])