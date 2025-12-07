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

    return splits


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
    splits = propagate_beam(mfld)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(splits)
    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()