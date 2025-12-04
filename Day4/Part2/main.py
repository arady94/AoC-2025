#!/usr/bin/env python3
from copy import deepcopy

def get_input(filename:str):
    with open(filename,'r') as f_in:
        input_sequence = f_in.readlines()

    return [seq.rstrip() for seq in input_sequence]


def find_removable_rolls(sequence:str):
    rows = len(sequence)
    cols = len(sequence[0])
    removable = 0

    viz = deepcopy(sequence)

    for row in range(rows):
        for col in range(cols):
            if sequence[row][col] in ['.','x']:
                continue

            neighbors = 0
            search = {'up':True, 'down':True, 'right':True, 'left':True,
                      'up-right':True, 'up-left':True, 'down-right':True, 'down-left':True}
            if col == 0:
                search['left'] = False
                search['up-left'] = False
                search['down-left'] = False
            if col == (cols-1):
                search['right'] = False
                search['up-right'] = False
                search['down-right'] = False
            if row == 0:
                search['up'] = False
                search['up-right'] = False
                search['up-left'] = False
            if row == (rows-1):
                search['down'] = False
                search['down-right'] = False
                search['down-left'] = False

            # print(f"({row},{col})\t{search}")
            hits = []
            for dir,valid in search.items():
                if not valid:
                    continue
                if dir == 'left' and sequence[row][col-1] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'right' and sequence[row][col+1] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'up' and sequence[row-1][col] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'down' and sequence[row+1][col] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'up-right' and sequence[row-1][col+1] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'down-right' and sequence[row+1][col+1] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'up-left' and sequence[row-1][col-1] == '@':
                    neighbors += 1
                    hits.append(dir)
                elif dir == 'down-left' and sequence[row+1][col-1] == '@':
                    neighbors += 1
                    hits.append(dir)
            
            # print(hits)

            if neighbors < 4:
                removable += 1
                char_list = list(viz[row])
                char_list[col] = 'x'
                viz[row] = "".join(char_list)
                sequence[row] = "".join(char_list)


    return removable, viz


if __name__ == "__main__":
    input = get_input('../data/input.txt')
    print(input)
    total = 0
    removed = -1
    while (removed != 0):
        removed, input = find_removable_rolls(input)
        total += removed
        print(removed)

    print()
    print(total)
    print()
    # for line in viz:
    #     print(line)
