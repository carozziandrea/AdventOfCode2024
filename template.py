##AOC DayXX

day = "XX"

#Part 1

import time
start = time.perf_counter()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        print(line.strip())

end = time.perf_counter()
print(f'Part 1: ')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        print(line.strip())

end = time.perf_counter()
print(f'Part 2: ')
print(f'\t {((end - start) * 10**3):.3f} ms')