#!/usr/bin/env python3
import time
from collections import defaultdict, deque
import numpy as np
from itertools import combinations


def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [[int(axis) for axis in line.rstrip().split(',')] for line in input_sequence]


def get_max_area(coords:list):
    all_pairs = combinations(coords,2)
    
    def get_area(pair):
        p1, p2 = pair[:]
        dx, dy = 1+abs(p1[0]-p2[0]), 1+abs(p1[1]-p2[1])
        return dx*dy

    max_area = 0
    max_pair = []
    for _, pair in enumerate(all_pairs):
        area = get_area(pair)
        if area > max_area:
            max_area = area
            max_pair = list(pair)

    return max_area, max_pair


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    coords = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    # print(coords)
    
    # Biggest Rect
    t0 = time.perf_counter()
    max_area, max_pair = get_max_area(coords)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(max_pair)
    print(max_area)

    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()