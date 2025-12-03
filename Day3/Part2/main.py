#!/usr/bin/env python3

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [seq.rstrip() for seq in input_sequence]


def get_max_joltage(sequence:str, n_cells:int):
    max_digits = []
    curr_cells = 0
    start_idx = 0
    end_idx = len(sequence) - n_cells + 1
    while (curr_cells < n_cells):
        # print(f"({start_idx},{end_idx})")
        print(f"{sequence[:start_idx]}[{sequence[start_idx:end_idx]}]{sequence[end_idx:]}")
        max_dig, max_loc = get_cell(sequence, start_idx, end_idx)
        print(f"{max_dig}")
        max_digits.append(f"{max_dig}")
        curr_cells += 1

        start_idx = max_loc+1

        need = n_cells - curr_cells
        avail = len(sequence) - (start_idx)

        end_idx = start_idx+(avail-need)+1 # max/min of this with something else

        if start_idx == end_idx:
            max_digits.append(sequence[start_idx:(start_idx+n_cells-curr_cells)])
            break
    
    jolt = int(''.join([dig for dig in max_digits]))
        
    print(jolt)

    return jolt


def get_cell(sequence:str, start_idx:int, end_idx:int):
    max_dig = max([int(digit) for digit in sequence[start_idx:end_idx]])
    max_loc = start_idx + sequence[start_idx:end_idx].index(f'{max_dig}')

    return max_dig, max_loc


if __name__ == "__main__":
    input = get_input('../data/input.txt')
    print(input)
    total = 0
    for seq in input:
        total += get_max_joltage(seq, 12)

    print()
    print(total)
