##AOC Day05

import time
import math
day = "05"

#Part 1
start = time.perf_counter()

rules_map = {}
inverted_rules_map = {}
solution = []
incorrect = []

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    content = file.read()
    sections = content.split("\n\n")

    rules = sections[0].split('\n')
    updates = sections[1].split('\n')

    #Parse rules
    for r in rules:
        rule = r.split('|')
        if rule[0] in rules_map:
            rules_map.update({rule[0]:rules_map[rule[0]] + [rule[1]]})
        else:
            rules_map.update({rule[0]:[rule[1]]})
        if rule[1] in inverted_rules_map:
            inverted_rules_map.update({rule[1]:inverted_rules_map[rule[1]] + [rule[0]]})
        else:
            inverted_rules_map.update({rule[1]:[rule[0]]})

    #Parse updates
    for u in updates:
        found = []
        update = u.split(',')
        for i in range(0, len(update)):
            num = update[i]
            found.append(all(num in rules_map and next in rules_map[num] for next in update[i+1:]))
        if False not in found:
            solution.append(int(update[math.floor(len(update)/2)]))
        else:
            incorrect.append(update)

    part1 = sum(solution)

end = time.perf_counter()
print(f'Part 1: {part1}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()
solution = []

for inc in incorrect:
    for j in range(0, len(inc)):
        for i in range(j+1, len(inc)):
            if inc[j] in rules_map:
                if inc[i] not in rules_map[inc[j]]:
                    inc[i], inc[j] = inc[j], inc[i]
            elif inc[j] in inverted_rules_map:
                if inc[i] in inverted_rules_map[inc[j]]:
                    inc[i], inc[j] = inc[j], inc[i]
    solution.append(int(inc[math.floor(len(inc)/2)]))

part2 = sum(solution)
end = time.perf_counter()
print(f'Part 2: {part2}')
print(f'\t {((end - start) * 10**3):.3f} ms')