#!/usr/bin/env python3


def get_input(filename: str):
    with open(filename, 'r') as f_in:
        input_sequence = f_in.readlines()
    return [[int(axis) for axis in line.rstrip().split(',')] for line in input_sequence]


def visualize_ascii(coords, width=80, height=40):
    """Quick ASCII visualization"""
    x_vals = [p[0] for p in coords]
    y_vals = [p[1] for p in coords]
    
    min_x, max_x = min(x_vals), max(x_vals)
    min_y, max_y = min(y_vals), max(y_vals)
    
    print(f"Range: x=[{min_x}, {max_x}], y=[{min_y}, {max_y}]")
    print(f"Points: {len(coords)}")
    print(f"Sparsity: {len(coords) / (max_x - min_x):.4f} points per x-unit\n")
    
    # Map to ASCII grid
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    
    for x, y in coords:
        # Scale to fit in ASCII grid
        col = int((x - min_x) / (max_x - min_x) * (width - 1))
        row = int((y - min_y) / (max_y - min_y) * (height - 1))
        grid[height - 1 - row][col] = '#'
    
    for row in grid:
        print(''.join(row))


if __name__=="__main__":
    coords = get_input('../data/input.txt')
    
    visualize_ascii(coords)
