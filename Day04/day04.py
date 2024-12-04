##AOC Day04

import time
day = "04"

#Part 1
start = time.perf_counter()

xmas = ['X', 'M', 'A', 'S']
matrix = []

def findWord(matrix, oi, oj, x):
    i = oi
    j = oj
    counter = 0
    #Top Left
    while i-1 >= 0 and j-1 >= 0 and x < len(xmas) and matrix[i-1][j-1] == xmas[x]:
        x += 1
        i -= 1
        j -= 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Top
    while i-1 >= 0 and x < len(xmas) and matrix[i-1][j] == xmas[x]:
        x += 1
        i -= 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Top Right
    while i-1 >= 0 and j+1 < len(matrix[0]) and x < len(xmas) and matrix[i-1][j+1] == xmas[x]:
        x += 1
        i -= 1
        j += 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Left
    while j-1 >= 0 and x < len(xmas) and matrix[i][j-1] == xmas[x]:
        x += 1
        j -= 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Right
    while j+1 < len(matrix[0]) and x < len(xmas) and matrix[i][j+1] == xmas[x]:
        x += 1
        j += 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Bottom left
    while i+1 < len(matrix) and j-1 >= 0 and x < len(xmas) and matrix[i+1][j-1] == xmas[x]:
        x += 1
        i += 1
        j -= 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Bottom
    while i+1 < len(matrix) and x < len(xmas) and matrix[i+1][j] == xmas[x]:
        x += 1
        i += 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    #Bottom right
    while i+1 < len(matrix) and j+1 < len(matrix[0]) and x < len(xmas) and matrix[i+1][j+1] == xmas[x]:
        x += 1
        i += 1
        j += 1
    if x == 4:
        counter += 1
    x = 1
    i = oi
    j = oj

    return counter

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        matrix.append(line.strip())

result = 0
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 'X':
            result += findWord(matrix, i, j, 1)

end = time.perf_counter()
print(f'Part 1: {result}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

xmas = ['M', 'A', 'S']
matrix = []

def findWordMAS(matrix, oi, oj, x):
    i = oi
    j = oj

    a_i = -1
    a_j = -1

    solutions = []
    #Top Left
    while i-1 >= 0 and j-1 >= 0 and x < len(xmas) and matrix[i-1][j-1] == xmas[x]:
        if xmas[x] == 'A':
            a_i = i-1
            a_j = j-1
        x += 1
        i -= 1
        j -= 1
    if x == 3:
        solutions.append((a_i, a_j))
    else: 
        a_i = -1;
        a_j = -1;
    x = 1
    i = oi
    j = oj

    #Top Right
    while i-1 >= 0 and j+1 < len(matrix[0]) and x < len(xmas) and matrix[i-1][j+1] == xmas[x]:
        if xmas[x] == 'A':
            a_i = i-1
            a_j = j+1
        x += 1
        i -= 1
        j += 1
    if x == 3:
        solutions.append((a_i, a_j))
    else: 
        a_i = -1;
        a_j = -1;
    x = 1
    i = oi
    j = oj

    #Bottom left
    while i+1 < len(matrix) and j-1 >= 0 and x < len(xmas) and matrix[i+1][j-1] == xmas[x]:
        if xmas[x] == 'A':
            a_i = i+1
            a_j = j-1
        x += 1
        i += 1
        j -= 1
    if x == 3:
        solutions.append((a_i, a_j))
    else: 
        a_i = -1;
        a_j = -1;
    x = 1
    i = oi
    j = oj

    #Bottom right
    while i+1 < len(matrix) and j+1 < len(matrix[0]) and x < len(xmas) and matrix[i+1][j+1] == xmas[x]:
        if xmas[x] == 'A':
            a_i = i+1
            a_j = j+1
        x += 1
        i += 1
        j += 1
    if x == 3:
        solutions.append((a_i, a_j))
    else: 
        a_i = -1;
        a_j = -1;
    x = 1
    i = oi
    j = oj

    return solutions

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        matrix.append(line.strip())

result = {}
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[0])):
        if matrix[i][j] == 'M':
            coord = findWordMAS(matrix, i, j, 1)
            for c in coord:
                if c in result:
                    result.update({c:result[c]+1})
                else:
                    result.update({c:1})

mas = 0
for c in result.values():
    if c > 1:
        mas += 1

end = time.perf_counter()
print(f'Part 2: {mas}')
print(f'\t {((end - start) * 10**3):.3f} ms')