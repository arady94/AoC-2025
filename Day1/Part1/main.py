#!/usr/bin/env python3

from typing import List

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    # print(input_sequence[0])
    return input_sequence

def run_sequence(input_sequence:List[str], start = 50, upper = 99):
    dxn_multiplier = {'R':1, 'L':-1}
    curr = start
    zero_count = 0
    for input in input_sequence:
        if curr == 0:
            zero_count += 1

        dxn = input[0]
        count = int(input[1:])
        multiplier = dxn_multiplier[dxn]
        curr += (count * multiplier)
        # print(curr)
        curr = curr%(upper+1)
        # print(curr)
        # print()

    return zero_count


if __name__ == "__main__":
    input = get_input('../data/input.txt')
    pwd = run_sequence(input)
    print(pwd)
