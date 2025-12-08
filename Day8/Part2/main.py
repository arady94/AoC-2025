#!/usr/bin/env python3
import time
from collections import defaultdict, deque
import numpy as np
from itertools import combinations


def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [line.rstrip() for line in input_sequence]


def get_sorted_pairs_by_distnce(items:list):
    all_pairs = combinations(items,2)
    distances = []

    for pair_idx, pair in enumerate(all_pairs):
        p1 = np.array([int(x) for x in pair[0].split(',')])
        p2 = np.array([int(x) for x in pair[1].split(',')])
        d = np.linalg.norm(p2-p1)
        distances.append((pair, d))

    sorted_distances = sorted(distances,reverse=False,key=lambda d: d[1])
    pairs = [sorted_distances[i][0] for i in range(len(sorted_distances))]

    return pairs


def connect(pairs):
    min_set = set([coord for pair in pairs for coord in pair])
    running_set = set()
    for pair in pairs:
        running_set.add(pair[0])
        running_set.add(pair[1])
        if running_set == min_set:
            return pair
        
    return None


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    coords = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    # print(coords)
    
    # Closest Pairs
    t0 = time.perf_counter()
    sorted_pairs = get_sorted_pairs_by_distnce(coords)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    # print(sorted_pairs)

    # Make connections
    t0 = time.perf_counter()
    last_cxn = connect(sorted_pairs)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")

    print(last_cxn)
    print(int(last_cxn[0].split(',')[0])*int(last_cxn[1].split(',')[0]))

    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()