##AOC Day06

import time
import numpy as np
day = "06"

#Part 1

def turn90(curDir):
    dirs = ['up', 'right', 'down', 'left']
    index = (dirs.index(curDir)+1) % 4
    return dirs[index]

start = time.perf_counter()
matrix = {}
visited = set()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    i = 0
    j = 0

    for line in file:
        for c in line.strip():
            matrix[(i,j)] = c
            j += 1
        i += 1
        j = 0

    init_pos = next((k for k, v in matrix.items() if v == '^'), None)
    if init_pos	is None:
        print(f"Initial position not found")

    r, c = init_pos[0], init_pos[1]
    visited.add((r,c))
    dir = "up"
    while True:
        try:
            tempr, tempc = r, c
            match dir:
                case 'up':
                    tempr -= 1
                case 'down':
                    tempr += 1
                case 'left':
                    tempc -= 1
                case 'right':
                    tempc += 1
            ele = matrix[(tempr,tempc)]
            if ele == '#':
                    dir = turn90(dir)
            else:
                visited.add((r,c))
                r, c = tempr, tempc
        except KeyError as e:
            visited.add((r,c))
            break

end = time.perf_counter()
print(f'Part 1: {len(visited)}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

def load_matrix(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().strip().split('\n')
    # Determina la dimensione della matrice
    num_rows = len(lines)
    num_cols = max(len(line) for line in lines)
    # Crea una matrice vuota e riempi con i caratteri letti
    matrix = np.full((num_rows, num_cols), '.', dtype=str)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[i, j] = char
    return matrix

sum_values = 0
solutions = 0
visited = set()

for (k,v), e in matrix.items():
    r, c = init_pos[0], init_pos[1]
    dir = "up"
    if (k,v) == (6,3):
        pass
    if e != '#' and e != '^':
        matrix[(k,v)] = '#'
        while True:
            if sum_values > len(visited) + 1000:
                solutions += 1
                break
            try:
                tempr, tempc = r, c
                match dir:
                    case 'up':
                        tempr -= 1
                    case 'down':
                        tempr += 1
                    case 'left':
                        tempc -= 1
                    case 'right':
                        tempc += 1
                ele = matrix[(tempr,tempc)]
                if ele == '#':
                        dir = turn90(dir)
                else:
                    visited.add((r,c))
                    sum_values += 1
                    r, c = tempr, tempc
            except KeyError as e:
                #print(f'{k}, {v} - No Loop')
                visited.add((r,c))
                sum_values += 1
                break
        visited.clear()
        sum_values = 0
        matrix[(k,v)] = '.'


end = time.perf_counter()
print(f'Part 2: {solutions}')
print(f'\t {((end - start) * 10**3):.3f} ms')