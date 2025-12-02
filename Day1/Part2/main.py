#!/usr/bin/env python3

from typing import List

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    # print(input_sequence[0])
    return input_sequence

#### Broken ####
def run_sequence(input_sequence:List[str], start = 50, upper = 99):
    dxn_multiplier = {'R':1, 'L':-1}
    curr = start
    zero_crossings = 0
    for inp_line, input in enumerate(input_sequence):
        dxn = input[0]
        count = int(input[1:])
        multiplier = dxn_multiplier[dxn]

        full_rotations = count//(upper+1)
        if (multiplier > 0) and (count > (upper-curr)):
            # full_rotations = (upper-curr)//(upper+1)
            zero_crossings += full_rotations + 1
            print(f"Right crossing (line {inp_line}): {full_rotations + 1}")
        elif (multiplier < 0) and (count > curr):
            # full_rotations = (curr)//(upper+1)
            zero_crossings += full_rotations + 1
            print(f"Left crossing (line {inp_line}): {full_rotations + 1}")

        curr += (count * multiplier)
        # print(curr)
        curr = curr%(upper+1)
        # print(curr)
        # print(zero_count)
        # print()

    return zero_crossings

def run_sequence2(input_sequence:List[str], start = 50, upper = 99):
    dxn_multiplier = {'R':1, 'L':-1}
    curr = start
    zero_count = 0

    for inp_line, input in enumerate(input_sequence):
        dxn = input[0]
        count = int(input[1:])
        multiplier = dxn_multiplier[dxn]

        for i in range(count):
            curr += multiplier * 1
            if curr > 0:
                curr = curr%(upper+1)
            elif curr < 0:
                curr = (upper+1+curr)%(upper+1)

            if curr == 0:
                zero_count += 1
                # print(f"INC: {zero_count}")
            
            # print(curr)
        # print()

    return zero_count


if __name__ == "__main__":
    input = get_input('../data/input.txt')
    pwd = run_sequence2(input)
    print(pwd)
