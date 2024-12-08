##AOC Day09

import time
from itertools import zip_longest
day = "09"

def group_contiguous_characters(lst):
    files = []
    spaces = []
    current_group = [lst[0]]  # Start with the first element
    
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:  # If current is the same as previous
            current_group.append(lst[i])
        else:  # If it's different, save the current group and start a new one
            if current_group[0] == '.':
                spaces.append(current_group)
            else:
                files.append(current_group)
            current_group = [lst[i]]
    
    # Append the last group
    if current_group[0] == '.':
        spaces.append(current_group)
    else:
        files.append(current_group)
    return files, spaces

#Part 1
start = time.perf_counter()
id = 0
disk = []

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    while True:
        file_length = file.read(1)
        if not file_length:
            break
        else:
            for i in range(int(file_length)):
                disk.append(id)
                #print(id, end="")
            id += 1

        free_space = file.read(1)
        if not free_space:
            break
        else:
            for i in range(int(free_space)):
                disk.append('.')
                #print('.', end="")
    print()

#for index, value in enumerate(disk):
    #print(value, end="")
#print()

diskP2 = disk.copy()
#print(diskP2)

l = 0
r = len(disk)-1
part1 = 0
while True:
    if l > r:
        break
    if disk[l] == '.':
        if disk[r] != '.' and l < r:
            disk[l], disk[r] = disk[r], disk[l]
            l += 1
        else:
            r -= 1
    else:
        l += 1

for index, value in enumerate(disk):
    #print(value, end="")
    if value != '.':
        part1 += (index * int(value))
print()


end = time.perf_counter()
print(f'Part 1: {part1}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

files, spaces = group_contiguous_characters(diskP2)
result = []

#Print
for sublist1, sublist2 in zip_longest(files, spaces, fillvalue=[]):
    result.extend(sublist1)
    result.extend(sublist2)
for index, value in enumerate(result):
    print(value, end="")
print("\n")
result = []



lenSpaces = [len(space) for space in spaces]
insertIndex = [0 for space in spaces]

indexfile = len(files)-1
indexspaces = 0
curFile = files[indexfile]
curSpace = spaces[indexspaces]

for f in reversed(files):
    for ix, s in enumerate(spaces):
        #IF THERE'S SPACE
        if s.count('.') >= len(f):
            #FILL THE VOID
            #FILE GET '.'
            for i in range(len(f)):
                s[insertIndex[ix]] = f[i]
                f[i] = '.'
                insertIndex[ix] += 1
            break

    #PRINT
"""    for sublist1, sublist2 in zip_longest(files, spaces, fillvalue=[]):
        result.extend(sublist1)
        result.extend(sublist2)
    for index, value in enumerate(result):
        print(value, end="")
    print("\n")
    result = []"""




"""while(indexspaces < len(spaces) and indexfile >= 0):
    curFile = files[indexfile]
    curSpace = spaces[indexspaces]

    if len(curFile) <= lenSpaces[indexspaces] and curFile[0] != '.':
        for i in range(len(curFile)):
            curSpace[insertIndex[indexspaces]] = curFile[i]
            files[indexfile][i] = '.'
            #curSpace[1] -= 1
            insertIndex[indexspaces] += 1
            lenSpaces[indexspaces] -= 1
            if insertIndex[indexspaces] == len(curSpace):
                indexspaces += 1
        #files.pop(indexfile)
        indexfile = len(files)-1
        for sublist1, sublist2 in zip_longest(files, spaces, fillvalue=[]):
            result.extend(sublist1)
            result.extend(sublist2)
        for index, value in enumerate(result):
            print(value, end="")
        print("\n")
        result = []
    else:
        indexfile -= 1"""

    #if len(curFile) == lenSpaces[indexspaces]:
    #    indexfile = len(files)-1

result = []
part2 = 0
for sublist1, sublist2 in zip_longest(files, spaces, fillvalue=[]):
        result.extend(sublist1)
        result.extend(sublist2)
for index, value in enumerate(result):
    print(value, end="")
    if value != '.':
        part2 += (index * int(value))
print()

end = time.perf_counter()
print(f'Part 2: {part2}')
print(f'\t {((end - start) * 10**3):.3f} ms')