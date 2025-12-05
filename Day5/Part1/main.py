#!/usr/bin/env python3
import time

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    delim = input_sequence.index('\n')
    fresh_ranges, ingredients = [seq.rstrip() for seq in input_sequence[:delim]], [ing.rstrip() for ing in input_sequence[delim+1:]]

    return fresh_ranges, ingredients


def agg_ranges(ranges:list):
    ranges_list = []
    for ing_range in ranges:
        l, u = [int(x) for x in ing_range.split('-')]
        ranges_list.append(range(l,u+1))

    fresh_set = set(ranges_list)

    return fresh_set


def count_fresh(ranges_set:set, ingredients:list):
    fresh = 0
    for ing in ingredients:
        for ing_range in ranges_set:
            if int(ing) in ing_range:
                fresh += 1
                break

    return fresh


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    fresh_ranges, ingredients = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    print(fresh_ranges)
    print(ingredients)
    
    # Time range aggregation
    t0 = time.perf_counter()
    fresh_set = agg_ranges(fresh_ranges)
    t1 = time.perf_counter()
    print(f"Range aggregation: {(t1-t0)*1000:.3f} ms")
    
    print(fresh_set)
    
    # Time fresh counting
    t0 = time.perf_counter()
    fresh_count = count_fresh(fresh_set, ingredients)
    t1 = time.perf_counter()
    print(f"Fresh counting: {(t1-t0)*1000:.3f} ms")
    
    print()
    print(fresh_count)
    
    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()