##AOC Day01

#Part 1

import time
start = time.perf_counter()

list_1 = []
list_2 = []

with open('C:\\users\\andre\\Desktop\\AOC24\\Day01\\day01input.txt', 'r') as file:
    for line in file:
        nums = line.split("   ")
        list_1.append(int(nums[0].strip()))
        list_2.append(int(nums[1].strip()))

list_1.sort()
list_2.sort()

sum = 0
i = 0
while i < len(list_1):
    sum += abs(list_1[i] - list_2[i])
    i+=1

end = time.perf_counter()
print(f'Part 1: {str(sum)}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

list_1 = []
dict_2 = {}

with open('C:\\users\\andre\\Desktop\\AOC24\\Day01\\day01input.txt', 'r') as file:
    for line in file:
        nums = line.split("   ")
        num1 = int(nums[0].strip())
        num2 = int(nums[1].strip())

        list_1.append(num1)
        if(num2 not in dict_2):
            dict_2[num2] = 1
        else:
            dict_2[num2] = dict_2[num2]+1

sim_score = 0
for num in list_1:
    if num in dict_2:
        sim_score += (num * dict_2[num])

end = time.perf_counter()
print(f'Part 2: {str(sim_score)}')
print(f'\t {((end - start) * 10**3):.3f} ms')