##AOC Day17

import time
import re
day = "17"

def combo(operand, regA, regB, regC):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return regA
    elif operand == 5:
        return regB
    elif operand == 6:
        return regC
    else:
        print("ERROR: INVALID OPERAND")
        return -1

#Part 1
start = time.perf_counter()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
        #Initilize registers
        regA = int(re.search(r'\d+', file.readline().strip()).group())
        regB = int(re.search(r'\d+', file.readline().strip()).group())
        regC = int(re.search(r'\d+', file.readline().strip()).group())

        #Empty line
        file.readline()

        #Instructions
        instructions = re.findall(r'\d+', file.readline().strip())
        instructions = [int(i) for i in instructions]

instruction_pointer = 0
output = ''
while(instruction_pointer < len(instructions)-1):
    #OPCODE & OPERAND
    opcode = instructions[instruction_pointer]
    instruction_pointer += 1
    operand = instructions[instruction_pointer]
    instruction_pointer += 1

    #PARSE OPCODE
    #ADV - DIVISION
    if opcode == 0:
        num = regA
        den = 2 ** combo(operand, regA, regB, regC)
        div = num // den
        regA = div
    #BXL - BITWISE XOR
    elif opcode == 1:
        xor = regB ^ operand
        regB = xor
    #BST - MODULO
    elif opcode == 2:
        num = combo(operand, regA, regB, regC)
        regB = num % 8
    #JNZ - JUMP NOT ZERO
    elif opcode == 3:
        if regA != 0:
            instruction_pointer = operand * 2
    #BXC - REGB XOR REGC
    elif opcode == 4:
        regB = regB ^ regC
    #OUTPUT
    elif opcode == 5:
        res = combo(operand, regA, regB, regC) % 8
        #print(res, end=',')
        output += str(res) 
        output += ","
    #BDV - DIVISION
    elif opcode == 6:
        num = regA
        den = 2 ** combo(operand, regA, regB, regC)
        div = num // den
        regB = div
    #CDV - DIVISION
    elif opcode == 7:
        num = regA
        den = 2 ** combo(operand, regA, regB, regC)
        div = num // den
        regC = div

end = time.perf_counter()
print()
print(f'Part 1: {output[:len(output)-1]}')
print(f'\t {((end - start) * 10**3):.3f} ms')

#Part 2
start = time.perf_counter()

with open(f'Day{day}\\day{day}input.txt', 'r') as file:
    for line in file:
        pass

end = time.perf_counter()
print(f'Part 2: ')
print(f'\t {((end - start) * 10**3):.3f} ms')