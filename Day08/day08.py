##AOC Da08

import numpy as np
import time
from itertools import combinations
from collections import defaultdict
day = "08"

#Part 1
start = time.perf_counter()

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            print(matrix[i][j], end="")
        print()

def is_in_boundaries(matrix, row, col):
    rows, cols = matrix.shape
    return 0 <= row < rows and 0 <= col < cols

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    data = [list(line.strip()) for line in file if line.strip()]
    matrix = np.array(data, dtype='U1')

#Fill dictionary with characters:[set of positions]
antennas = defaultdict(list)
for (row, col), char in np.ndenumerate(matrix):
    if char != '.':
        antennas[char].append((row, col))

antis = set()
for char, positions in antennas.items():
    for first, second in combinations(positions, 2):
        rowdist = (second[0] - first[0])
        coldist = (second[1] - first[1])
        anti1pos = (first[0] - rowdist, first[1] - coldist)
        anti2pos = (second[0] + rowdist, second[1] + coldist)
        if is_in_boundaries(matrix, anti1pos[0], anti1pos[1]):
            matrix[anti1pos[0], anti1pos[1]] = '#'
            antis.add((anti1pos[0], anti1pos[1]))

        if is_in_boundaries(matrix, anti2pos[0], anti2pos[1]):
            matrix[anti2pos[0], anti2pos[1]] = '#'
            antis.add((anti2pos[0], anti2pos[1]))

end = time.perf_counter()
print(f'Part 1: {len(antis)}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

antis = set()
antis_len = 0
for char, positions in antennas.items():
    for first, second in combinations(positions, 2):
        rowdist = (second[0] - first[0])
        coldist = (second[1] - first[1])
        anti1pos = (first[0] - rowdist, first[1] - coldist)
        anti2pos = (second[0] + rowdist, second[1] + coldist)
        while is_in_boundaries(matrix, anti1pos[0], anti1pos[1]) or is_in_boundaries(matrix, anti2pos[0], anti2pos[1]):
            if is_in_boundaries(matrix, anti1pos[0], anti1pos[1]):
                matrix[anti1pos[0], anti1pos[1]] = '#'
                antis.add((anti1pos[0], anti1pos[1]))

            if is_in_boundaries(matrix, anti2pos[0], anti2pos[1]):
                matrix[anti2pos[0], anti2pos[1]] = '#'
                antis.add((anti2pos[0], anti2pos[1]))
            anti1pos = (anti1pos[0] - rowdist, anti1pos[1] - coldist)
            anti2pos = (anti2pos[0] + rowdist, anti2pos[1] + coldist)

count_a = np.sum(matrix != '.')

end = time.perf_counter()
print(f'Part 2: {count_a}')
print(f'\t {((end - start) * 10**3):.3f} ms')