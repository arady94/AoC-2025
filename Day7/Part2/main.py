#!/usr/bin/env python3
import time
from copy import deepcopy
import re


def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [line.rstrip() for line in input_sequence]


def propagate_beam(mfld:list):
    splits = 0
    
    for line_idx in range(0, len(mfld)-1):
        nxt_line = deepcopy(list(mfld[line_idx+1]))
        if 'S' in mfld[line_idx]:
            s_idx = mfld[line_idx].index('S')
            if nxt_line[s_idx] == '.':
                nxt_line[s_idx] = '|'
                mfld[line_idx+1] = ''.join(nxt_line)
            
            continue
        
        if '|' in mfld[line_idx]:
            # print(mfld[line_idx])
            beam_idcs = [x.start() for x in re.finditer('\|',mfld[line_idx])]
            for beam_idx in beam_idcs:
                nxt_stop = mfld[line_idx+1][beam_idx]
                if nxt_stop == '.':
                    nxt_line[beam_idx] = '|'
                    mfld[line_idx+1] = ''.join(nxt_line)
                elif nxt_stop == '^':
                    nxt_line[beam_idx-1] = '|'
                    nxt_line[beam_idx+1] = '|'
                    mfld[line_idx+1] = ''.join(nxt_line)
                    splits += 1

    
    for line in mfld:
        print(line)

    return splits, mfld


def count_paths(mfld:list):
    # paths = [1 if x=='|' else 0 for x in mfld[-1]]
    paths = [0] * len(mfld[-1])

    for line_idx in range(len(mfld)-1,1,-1):
        prev_line = deepcopy(mfld[line_idx-1])
        beam_idcs = [x.start() for x in re.finditer('\|',mfld[line_idx])]
        for beam_idx in beam_idcs:
            if beam_idx == 0:
                pass
            elif beam_idx == len(mfld[line_idx])-1:
                pass
            else:
                if (mfld[line_idx][beam_idx-1] == '^') and (prev_line[beam_idx-1] == '|'):
                    paths[beam_idx] += 1
                if (mfld[line_idx][beam_idx+1] == '^') and (prev_line[beam_idx+1] == '|'):
                    paths[beam_idx] += 1
        print(paths)
        time.sleep(2.5)
    print(paths)

    return paths


def count_paths2(mfld:list):
    def print_paths():
        for path in paths:
            print(path)

    paths = [[0]*len(mfld[-1]) for _ in range(len(mfld))]
    paths[0] = [1 if x=='S' else 0 for x in mfld[0]]
    # print_paths()
    # print()

    for line_idx in range(len(mfld)-1):
        # print(mfld[line_idx])
        # print_paths()

        for cell_idx in range(len(mfld[line_idx])):
            if mfld[line_idx+1][cell_idx] == '.':
                # print("######## EMPTY ########")
                paths[line_idx+1][cell_idx] += paths[line_idx][cell_idx]
            elif mfld[line_idx+1][cell_idx] == '^':
                # print("######## SPLIT ########")
                paths[line_idx+1][cell_idx-1] += paths[line_idx][cell_idx]
                # print(f"\n\n{paths[line_idx+1][cell_idx+1]}\n{paths[line_idx][cell_idx]}\n\n")
                paths[line_idx+1][cell_idx+1] += paths[line_idx][cell_idx]
                paths[line_idx+1][cell_idx] = 0
            else:
                continue
    
        # print(paths[line_idx])
        # time.sleep(0.5)
    print_paths()

    return paths


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    mfld = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    # print(mfld)
    
    # Time Propagation
    t0 = time.perf_counter()
    splits, propd_mfld = propagate_beam(deepcopy(mfld))
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(splits)

    # Time Counting
    t0 = time.perf_counter()
    paths = count_paths2(mfld)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")

    print(sum(paths[-1]))

    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()