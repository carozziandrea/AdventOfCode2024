##AOC Day02

import time
day = "02"

#Part 1
start = time.perf_counter()

def checkLine(nums):
    if len(nums) < 2:
        return True

    asc = True
    desc = True
    for i in range(1, len(nums)):
        a = int(nums[i-1])
        b = int(nums[i])

        if abs(a - b) > 3:
            return False
        if a == b:
            return False
        if a < b:
            desc = False
        if a > b:
            asc = False
        if not asc and not desc:
            return False
    return True

#Part 2
def canTolerate(levels):
    sub_levels = [levels[:i] + levels[i+1:] for i in range(0, len(levels))]
    #print(sub_levels)
    for s in sub_levels:
        if checkLine(s):
            #print(f'OK: {s}')
            return True
    return False

safeP1 = 0
safeP2 = 0
with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        levels = line.split()
        if checkLine(levels):
            safeP1 += 1
            safeP2 += 1
        elif canTolerate(levels):
            safeP2 += 1
            
end = time.perf_counter()
print(f'Part 1: {safeP1}')
print(f'Part 2: {safeP2}')
print(f'\t {((end - start) * 10**3):.3f} ms')