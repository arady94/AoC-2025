#!/usr/bin/env python3
import time
from itertools import combinations


def get_input(filename: str):
    with open(filename, 'r') as f_in:
        input_sequence = f_in.readlines()
    return [[int(axis) for axis in line.rstrip().split(',')] for line in input_sequence]


def compress_coordinates(coords):
    """Compress coordinate space to only use indices"""
    # Get all unique x and y values, sorted
    x_values = sorted(set(p[0] for p in coords))
    y_values = sorted(set(p[1] for p in coords))
    
    # Create mapping from original to compressed coordinates
    x_to_compressed = {x: i for i, x in enumerate(x_values)}
    y_to_compressed = {y: i for i, y in enumerate(y_values)}
    
    # Compress the polygon
    compressed_coords = [(x_to_compressed[p[0]], y_to_compressed[p[1]]) for p in coords]
    
    # Also need reverse mapping for area calculation
    compressed_to_x = {i: x for i, x in enumerate(x_values)}
    compressed_to_y = {i: y for i, y in enumerate(y_values)}
    
    return compressed_coords, compressed_to_x, compressed_to_y


def get_max_area(coords: list):
    # Compress coordinates
    print("Compressing coordinates...")
    compressed_coords, idx_to_x, idx_to_y = compress_coordinates(coords)
    
    print(f"Compressed space: {len(idx_to_x)}x{len(idx_to_y)}")
    
    # Precompute interior points in compressed space
    print("Computing interior points...")
    interior = precompute_interior(compressed_coords, len(idx_to_x), len(idx_to_y))
    print(f"Interior points: {len(interior)}")
    
    # Get all pairs and calculate their actual areas
    all_pairs = list(combinations(coords, 2))
    
    def get_real_area(pair):
        p1, p2 = pair
        dx = 1 + abs(p1[0] - p2[0])
        dy = 1 + abs(p1[1] - p2[1])
        return dx * dy
    
    # Sort by actual area (descending)
    sorted_pairs = sorted(all_pairs, key=get_real_area, reverse=True)
    print(f"Checking {len(sorted_pairs)} pairs...")
    
    # Create mapping for quick lookup
    coord_to_compressed = {tuple(coords[i]): compressed_coords[i] for i in range(len(coords))}
    
    def check_interior_compressed(pair):
        # Convert to compressed coordinates
        p1_comp = coord_to_compressed[tuple(pair[0])]
        p2_comp = coord_to_compressed[tuple(pair[1])]
        
        min_x, max_x = min(p1_comp[0], p2_comp[0]), max(p1_comp[0], p2_comp[0])
        min_y, max_y = min(p1_comp[1], p2_comp[1]), max(p1_comp[1], p2_comp[1])
        
        # Check all points in compressed rectangle
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                if (x, y) not in interior:
                    return False
        return True
    
    # Find first valid rectangle
    for i, pair in enumerate(sorted_pairs):
        if i % 1000 == 0:
            print(f"Checked {i} pairs...")
        
        if check_interior_compressed(pair):
            area = get_real_area(pair)
            print(f"Found valid rectangle with area {area}")
            return area, list(pair)
    
    return 0, []


def precompute_interior(compressed_coords, width, height):
    """Use scanline to find all interior points in compressed space"""
    interior = set()
    
    # Add boundary points
    n = len(compressed_coords)
    for i in range(n):
        p1 = compressed_coords[i]
        p2 = compressed_coords[(i + 1) % n]
        interior.add(p1)
        
        # Add points on edges
        x1, y1 = p1
        x2, y2 = p2
        
        if x1 == x2:  # Vertical edge
            for y in range(min(y1, y2), max(y1, y2) + 1):
                interior.add((x1, y))
        elif y1 == y2:  # Horizontal edge
            for x in range(min(x1, x2), max(x1, x2) + 1):
                interior.add((x, y1))
    
    # Scanline for interior points
    for y in range(height):
        # Find x coordinates where polygon crosses this scanline
        crossings = []
        
        for i in range(n):
            p1 = compressed_coords[i]
            p2 = compressed_coords[(i + 1) % n]
            x1, y1 = p1
            x2, y2 = p2
            
            # Check if edge spans this y coordinate
            if y1 != y2:  # Not horizontal
                if min(y1, y2) <= y < max(y1, y2):
                    # Calculate x at this y
                    t = (y - y1) / (y2 - y1)
                    x_cross = x1 + t * (x2 - x1)
                    crossings.append(x_cross)
        
        # Sort crossings
        crossings.sort()
        
        # Fill between pairs
        inside = False
        prev_x = None
        for x_cross in crossings:
            if inside and prev_x is not None:
                x_start = int(prev_x)
                x_end = int(x_cross)
                for x in range(x_start, x_end + 1):
                    interior.add((x, y))
            inside = not inside
            prev_x = x_cross
    
    return interior


def run():
    start_time = time.perf_counter()
    
    coords = get_input('../data/input.txt')
    print(f"Loaded {len(coords)} coordinates")
    
    max_area, max_pair = get_max_area(coords)
    
    print(f"\nMax pair: {max_pair}")
    print(f"Max area: {max_area}")
    
    end_time = time.perf_counter()
    print(f"\nTotal execution time: {(end_time-start_time):.3f} seconds")


if __name__ == "__main__":
    run()