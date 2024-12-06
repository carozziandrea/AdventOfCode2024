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

sum_values = 0
loop = False
solutions = 0
visited = set()
duplicates = {}

for (k,v), e in matrix.items():
    r, c = init_pos[0], init_pos[1]
    dir = "up"
    if e != '#' and e != '^':
        matrix[(k,v)] = '#'
        while True:
            if loop:
                loop = False
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
                        duplicates[(r,c)] = duplicates.get((r,c), 0) + 1
                        if duplicates[(r,c)] == 5:
                            loop = True
                else:
                    r, c = tempr, tempc
            except KeyError as e:
                break
        duplicates.clear()
        matrix[(k,v)] = '.'


end = time.perf_counter()
print(f'Part 2: {solutions}')
print(f'\t {((end - start) * 10**3):.3f} ms')