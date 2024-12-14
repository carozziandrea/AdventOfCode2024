##AOC Day14

import time
import numpy as np
import re
from robot import Robot

day = "14"

def printMatrixToFile(second, matrix):
    with open(f'Day{day}\\day{day}output.txt', 'a') as f:
        print(second, file=f)
        for i in range(cols):
            for j in range(rows):
                if matrix[i][j] == 0:
                    print(' ', file=f,end='')
                else:
                    print('O', file=f,end='')
            print('', file=f)

#Part 1
start = time.perf_counter()

cols = 103
rows = 101
matrix = np.zeros((cols,rows), dtype=int)
#print(matrix)

startC, startR = 0,0
robots = []

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        coordinates = re.findall(r'-?\d+', line)
        (posC, posR) = (int(coordinates[0]), int(coordinates[1]))
        (velC, velR) = (int(coordinates[2]), int(coordinates[3]))
        newr = Robot((posC, posR), (velC, velR))
        robots.append(newr)
        print((posC, posR))
        matrix[posR][posC] += 1

#print(matrix)

seconds = 6356
for s in range(seconds):
    for r in robots:
        (curC, curR) = r.getCurrentPosition()
        (velC, velR) = r.getVelocity()
        matrix[curR][curC] -= 1
        newC = (curC + velC) % rows
        newR = (curR + velR) % cols
        matrix[newR][newC] += 1
        r.setCurrentPosition((newC, newR))
    print(f'\nSecond: {s+1}')
    #printMatrixToFile(s,matrix)

print(matrix)

# Selezione dei quadranti
top_left = matrix[:51, :50]        # Quadrante in alto a sinistra
top_right = matrix[:51, 51:]       # Quadrante in alto a destra
bottom_left = matrix[52:, :50]     # Quadrante in basso a sinistra
bottom_right = matrix[52:, 51:]    # Quadrante in basso a destra

safety_factor = np.sum(top_left) * np.sum(top_right) * np.sum(bottom_left) * np.sum(bottom_right)

end = time.perf_counter()
print(f'Part 1: {safety_factor}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

end = time.perf_counter()
print(f'Part 2: ')
print(f'\t {((end - start) * 10**3):.3f} ms')