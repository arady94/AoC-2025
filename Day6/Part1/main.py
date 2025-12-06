#!/usr/bin/env python3
import time
import math


def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [seq.rstrip().lstrip() for seq in input_sequence[:-1]], input_sequence[-1].lstrip().rstrip()


def run_arithmetic(lines:list, ops:list):
    total = 0
    for op_idx, op in enumerate(ops.split()):
        eqn_res = 0
        # print([line.split()[op_idx] for line in lines])
        elements = [line.split()[op_idx] for line in lines]
        if op == '*':
            eqn_res = math.prod([int(el) for el in elements])
        elif op == '+':
            eqn_res = sum([int(el) for el in elements])

        total += eqn_res

    return total


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    nums, ops = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    # print(nums)
    # print(ops)
    
    # Time range aggregation
    t0 = time.perf_counter()
    total = run_arithmetic(nums, ops)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(total)
    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()