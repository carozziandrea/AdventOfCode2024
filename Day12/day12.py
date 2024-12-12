##AOC Day12

import time
day = "12"

def isWithinBoundaries(matrix, r, c):
    rows = len(matrix)         # Number of rows
    cols = len(matrix[0]) if rows > 0 else 0  # Number of columns
    return 0 <= r < rows and 0 <= c < cols


#Part 1
start = time.perf_counter()
garden = []
with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        garden.append([*line.strip()])
        #print(line.strip())

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
]

to_Visit = set()
visited = set()
per = 0
area = 0
regions = []
for ri, r in enumerate(garden):
    for ci, c in enumerate(r):
        if((ri,ci)) not in visited and (ri,ci) not in to_Visit:
            to_Visit.add((ri,ci))
            while to_Visit:
                area += 1
                (curRow, curCol) = to_Visit.pop()
                curChar = garden[curRow][curCol]
                visited.add((curRow, curCol))

                for dir in directions:
                    newr, newc = curRow + dir[0], curCol + dir[1]
                    if isWithinBoundaries(garden, newr, newc):
                        if garden[newr][newc] == curChar:
                            if (newr, newc) not in visited:
                                to_Visit.add((newr, newc))
                        else:
                            per += 1
                    else:
                        per += 1
            print(f'Char: {curChar} - Area: {area} - Perimeter: {per}')
            regions.append((area,per))
            area = 0
            per = 0

result = 0
for region in regions:
    result += (region[0] * region[1])

end = time.perf_counter()
print(f'Part 1: {result}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        pass

end = time.perf_counter()
print(f'Part 2: ')
print(f'\t {((end - start) * 10**3):.3f} ms')