##AOC Day03

import time
import re
day = "03"

#Part 1
start = time.perf_counter()

pattern = r"mul\(\d{1,3},\d{1,3}\)"
patternDigits = r"\d{1,3}"
result = 0

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    content = file.read()
    matches = re.findall(pattern, content)

    for match in matches:
        digits = re.findall(patternDigits, match)
        result += (int(digits[0]) * int(digits[1]))

end = time.perf_counter()
print(f'Part 1: {result}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()
pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
patternDigits = r"\d{1,3}"
result = 0
can_execute = True

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    content = file.read()
    matches = re.findall(pattern, content)

    for match in matches:
        if can_execute:
            if match.startswith("mul"):
                digits = re.findall(patternDigits, match)
                result += (int(digits[0]) * int(digits[1]))
            elif match == "don't()":
                can_execute = False
        elif match == "do()":
                can_execute = True

end = time.perf_counter()
print(f'Part 2: {result}')
print(f'\t {((end - start) * 10**3):.3f} ms')