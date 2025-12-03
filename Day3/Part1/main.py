#!/usr/bin/env python3

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [seq.rstrip() for seq in input_sequence]


def get_max_joltage(sequence:str):
    sequence_reverse = sequence[::-1]
    max1 = -1
    for idx, digit in enumerate(sequence_reverse):
        if idx == 0:
            continue

        if int(digit) >= max1:
            max1 = int(digit)
            idx1 = idx

    max2 = -1
    for idx, digit in enumerate(sequence_reverse[:idx1]):
        if (int(digit) >= max2):
            max2 = int(digit)

    jolt = int(f"{max1}{max2}")
        
    print(jolt)

    return jolt


if __name__ == "__main__":
    input = get_input('../data/input.txt')
    print(input)
    total = 0
    for seq in input:
        total += get_max_joltage(seq)

    print()
    print(total)
