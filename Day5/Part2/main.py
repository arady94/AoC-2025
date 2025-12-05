#!/usr/bin/env python3
import time
from itertools import combinations
from typing import List
from tqdm import tqdm

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    delim = input_sequence.index('\n')
    fresh_ranges, ingredients = [seq.rstrip() for seq in input_sequence[:delim]], [ing.rstrip() for ing in input_sequence[delim+1:]]

    return fresh_ranges, ingredients


def agg_ranges(ranges:list)->List[range]:
    ranges_list = []
    for ing_range in ranges:
        l, u = [int(x) for x in ing_range.split('-')]
        ranges_list.append(range(l,u+1))

    return ranges_list


def trim_ranges(ranges:List[range]):
    range_combos = combinations(ranges,2)
    # print(list(range_combos))
    cull_indices = []
    replacements = []
    for range_pair in tqdm(range_combos):
        p1, p2 = range_pair[:]
        # print(f"{p1},{p2}")
        if p1.start in p2 and p1.stop in p2:
            cull_indices.append(ranges.index(p1))
        elif p2.start in p1 and p2.stop in p1:
            cull_indices.append(ranges.index(p2))
        elif p1.start in p2:
            cull_indices = cull_indices + [ranges.index(p1), ranges.index(p2)]
            replacements.append(range(p2.start, p1.stop))
        elif p2.start in p1:
            cull_indices = cull_indices + [ranges.index(p1), ranges.index(p2)]
            replacements.append(range(p1.start, p2.stop))

    minimal_ranges = [ing_range for ing_range in ranges if ranges.index(ing_range) not in set(cull_indices)] + list(set(replacements)) # set() is crucial here to avoid massive growth. there *will* be duplicates

    if len(minimal_ranges) > len(ranges):
        print(f"#################")
        print(f"Detected growth from {len(ranges)} to {len(minimal_ranges)}")
        print(f"Cull List ({len(set(cull_indices))})")
        print(f"Replacement List ({len(set(replacements))})")
        print(f"#################")
        # return []

    return minimal_ranges


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    fresh_ranges, _ = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    # Time range aggregation
    t0 = time.perf_counter()
    fresh_set = agg_ranges(fresh_ranges)
    t1 = time.perf_counter()
    print(f"Range aggregation: {(t1-t0)*1000:.3f} ms")
    print(f"Initial range count: {len(fresh_set)}")
    
    # Time first trim
    print("\nFirst trim pass:")
    t0 = time.perf_counter()
    fresh_set_trim = trim_ranges(fresh_set)
    t1 = time.perf_counter()
    print(f"First trim: {(t1-t0)*1000:.3f} ms")
    
    min_size = len(fresh_set_trim)
    iteration = 1
    trim_times = []
    
    # Time iterative trimming
    while(True):
        print(f"\nTrim iteration {iteration + 1}:")
        t0 = time.perf_counter()
        fresh_set_trim = trim_ranges(fresh_set_trim)
        t1 = time.perf_counter()
        trim_time = (t1-t0)*1000
        trim_times.append(trim_time)
        print(f"Trim time: {trim_time:.3f} ms")
        
        if len(fresh_set_trim) == min_size:
            print(f"Converged at {min_size} ranges")
            break
        else:
            print(f"Trim from {min_size} -> {len(fresh_set_trim)}")
            min_size = len(fresh_set_trim)
        
        iteration += 1

    print()
    print(f"Final range sum: {sum([len(x) for x in fresh_set_trim])}")
    
    # Summary statistics
    end_time = time.perf_counter()
    print(f"\n{'='*50}")
    print(f"Total iterations: {iteration + 1}")
    if trim_times:
        print(f"Average trim time (after first): {sum(trim_times)/len(trim_times):.3f} ms")
    print(f"Total execution time: {(end_time-start_time)*1000:.3f} ms ({(end_time-start_time):.3f} s)")
    print(f"{'='*50}")


if __name__ == "__main__":
    run()