#!/usr/bin/env python3
import time
from collections import defaultdict, deque
import numpy as np
from itertools import combinations


def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [line.rstrip() for line in input_sequence]


def get_closest_pairs(items:list, n_pairs:int):
    all_pairs = combinations(items,2)
    distances = []

    for pair_idx, pair in enumerate(all_pairs):
        p1 = np.array([int(x) for x in pair[0].split(',')])
        p2 = np.array([int(x) for x in pair[1].split(',')])
        d = np.linalg.norm(p2-p1)
        distances.append((pair, d))

    sorted_distances = sorted(distances,reverse=False,key=lambda d: d[1])
    pairs = [sorted_distances[i][0] for i in range(min(n_pairs,len(sorted_distances)))]

    return pairs


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    coords = get_input('../data/test.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    print(coords)
    
    # Closest Pairs
    t0 = time.perf_counter()
    n_closest_pairs = get_closest_pairs(coords, n_pairs=10)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(n_closest_pairs)
    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()