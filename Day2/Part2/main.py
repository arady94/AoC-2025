#!/usr/bin/env python3

from typing import List
import re

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.read()

    # print(input_sequence[0])
    return input_sequence.split(',')

def ranges_to_strs(ranges:List[str]):
    range_strs = []
    for id_range in ranges:
        start, end = [int(x) for x in id_range.split('-')]
        range_strs.append([f'{x}' for x in list(range(start,end+1))])
        
    return range_strs

def get_matches(input, pattern = r"^(\d+)\1+$"):
    # print(input)
    winners = []
    for x in input:
        # print(x)
        matches = re.search(pattern, x)
        # print(matches)
        if matches is not None:
            winners.append(x)

    return winners



if __name__ == "__main__":
    input = get_input('../data/input.txt')
    # print(input)
    range_strs = ranges_to_strs(input)
    # print(range_strs)
    
    # winners = get_matches(range_strs[1])
    # print(winners)
    #     
    total = 0
    for range_str in range_strs:
        winners = get_matches(range_str)
        print(winners)
        total += sum([int(x) for x in winners])
    print()
    print(total)
