#!/usr/bin/env python3

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
    fresh_ranges, ingredients = get_input('../data/input.txt')
    print(fresh_ranges)
    print(ingredients)
    fresh_set = agg_ranges(fresh_ranges)
    print(fresh_set)
    fresh_count = count_fresh(fresh_set, ingredients)
    print()
    print(fresh_count)


if __name__ == "__main__":
    run()