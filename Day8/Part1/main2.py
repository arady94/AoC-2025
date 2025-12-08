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


def find_n_largest_circuits(connections, n):
    """
    Find the n largest circuits (connected components) after making connections.
    This uses Union-Find to efficiently track which junction boxes are connected.
    """
    # Union-Find data structure
    parent = {}
    size = {}
    
    # Get all nodes
    all_nodes = set()
    for a, b in connections:
        all_nodes.add(a)
        all_nodes.add(b)
    
    # Initialize: each node is its own parent
    for node in all_nodes:
        parent[node] = node
        size[node] = 1
    
    def find(x):
        """Find root of x with path compression"""
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        """Union two sets"""
        root_x = find(x)
        root_y = find(y)
        
        if root_x == root_y:
            return  # Already in same circuit
        
        # Union by size: attach smaller tree to larger
        if size[root_x] < size[root_y]:
            parent[root_x] = root_y
            size[root_y] += size[root_x]
        else:
            parent[root_y] = root_x
            size[root_x] += size[root_y]
    
    # Process all connections
    for a, b in connections:
        union(a, b)
    
    # Find all circuit sizes
    circuit_sizes = defaultdict(int)
    for node in all_nodes:
        root = find(node)
        circuit_sizes[root] += 1
    
    # Get the n largest circuits
    sizes = sorted(circuit_sizes.values(), reverse=True)
    return sizes[:n]


def run():
    start_time = time.perf_counter()
    
    # Time input reading
    t0 = time.perf_counter()
    coords = get_input('../data/input.txt')
    t1 = time.perf_counter()
    print(f"Input reading: {(t1-t0)*1000:.3f} ms")
    
    print(coords)
    
    # Closest Pairs
    t0 = time.perf_counter()
    n_closest_pairs = get_closest_pairs(coords, n_pairs=1000)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(n_closest_pairs)

    # Chains
    t0 = time.perf_counter()
    largest_circuits = find_n_largest_circuits(n_closest_pairs, n=3)
    t1 = time.perf_counter()
    print(f"Evaluation: {(t1-t0)*1000:.3f} ms")
    
    print(largest_circuits)

    print("Largest circuit sizes:")
    print("=" * 60)
    for i, size in enumerate(largest_circuits, 1):
        print(f"Circuit {i}: {size} junction boxes")

    print(f"\nProduct of three largest: {largest_circuits[0] * largest_circuits[1] * largest_circuits[2]}")

    # # Show which nodes are in which circuit
    # print("\n" + "=" * 60)
    # print("Circuit membership:")
    # print("=" * 60)

    # parent = {}
    # all_nodes = set()
    # for a, b in n_closest_pairs:
    #     all_nodes.add(a)
    #     all_nodes.add(b)

    # for node in all_nodes:
    #     parent[node] = node

    # def find(x):
    #     if parent[x] != x:
    #         parent[x] = find(parent[x])
    #     return parent[x]

    # def union(x, y):
    #     root_x = find(x)
    #     root_y = find(y)
    #     if root_x != root_y:
    #         parent[root_x] = root_y

    # for a, b in n_closest_pairs:
    #     union(a, b)

    # circuits = defaultdict(list)
    # for node in sorted(all_nodes):
    #     root = find(node)
    #     circuits[root].append(node)

    # for i, (root, members) in enumerate(sorted(circuits.items(), key=lambda x: len(x[1]), reverse=True), 1):
    #     print(f"\nCircuit {i} ({len(members)} boxes):")
    #     for member in members:
    #         print(f"  {member}")

    # print(f"\nProduct of three largest: {largest_circuits[0] * largest_circuits[1] * largest_circuits[2]}")

    # Total time
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time)*1000:.3f} ms")


if __name__ == "__main__":
    run()