import time
from collections import deque

day = "10"

# Part 1
start = time.perf_counter()

def bfs(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start[0], start[1], [matrix[start[0]][start[1]]])])
    visited = set()

    visited.add((start[0], start[1], tuple([matrix[start[0]][start[1]]])))

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == end:
            if sorted(path) == list(range(10)):
                return path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if matrix[nr][nc] > path[-1]:
                    new_path = path + [matrix[nr][nc]]
                    new_state = (nr, nc, tuple(new_path))

                    if new_state not in visited:
                        queue.append((nr, nc, new_path))
                        visited.add(new_state)

    return None

# Carica la matrice dal file
matrix = []
with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        matrix.append(list(map(int, line.strip())))

# Trova le posizioni dei "trailheads"
trailheads = []
endings = []
for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if matrix[r][c] == 0:
            trailheads.append((r, c))
        elif matrix[r][c] == 9:
            endings.append((r, c))

# Calcola il punteggio totale
score = 0
for head in trailheads:
    for end in endings:
        path = bfs(matrix, head, end)
        if path:
            score += 1

end = time.perf_counter()
print(f'Part 1: {score}')
print(f'\t {((end - start) * 10**3):.3f} ms')

# Part 2
start = time.perf_counter()

def bfs_part2(matrix, start, end):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start[0], start[1], [matrix[start[0]][start[1]]])])
    valid_paths = []

    while queue:
        r, c, path = queue.popleft()

        if (r, c) == end:
            if sorted(path) == list(range(10)):
                valid_paths.append(path)
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if matrix[nr][nc] > path[-1]:
                    new_path = path + [matrix[nr][nc]]
                    queue.append((nr, nc, new_path))

    return valid_paths

score = 0
for head in trailheads:
    for end in endings:
        paths = bfs_part2(matrix, head, end)
        score += len(paths)

end = time.perf_counter()
print(f'Part 2: {score}')
print(f'\t {((end - start) * 10**3):.3f} ms')