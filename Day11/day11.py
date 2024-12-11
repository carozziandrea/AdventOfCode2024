##AOC Day11

import time
from functools import lru_cache
day = "11"

@lru_cache(maxsize=None)
def single_blink_stone(value):
    text = str(value)
    num_of_digits = len(text)
    if value == 0:
        return (1, None)
    elif num_of_digits % 2 == 0:
        mid_point = num_of_digits // 2
        left_stone = int(text[:mid_point])
        right_stone = int(text[mid_point:])
        return (left_stone, right_stone)
    else:
        return (value * 2024, None)

@lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):
    left_stone, right_stone = single_blink_stone(stone)
    if depth == 1:
        if right_stone is None:
            return 1
        else:
            return 2

    else:
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        return output

def run(count):
    output = 0
    for stone in stones:
        output += count_stone_blinks(stone, count)
    return output

#Part 1-2
start = time.perf_counter()
stones = []

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        for n in line.split(" "):
           stones.append(int(n))


print(f'Part 1: {run(25)}')
print(f'Part 2: {run(75)}')