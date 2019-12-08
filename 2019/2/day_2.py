#!/usr/bin/env python3

import math
import sys

input = open(sys.argv[1], "r")
raw  = input.readline().split(",")
initial_program = [ int(r) for r in raw ]

# program[1] = 12
# program[2] = 2

desired_output = 19690720

print(initial_program)
print()

for noun in range(100):
    for verb in range(100):
        program = list(initial_program)
        program[1] = noun
        program[2] = verb

        position = 0
        while True:
            op1 = program[program[position+1]]
            op2 = program[program[position+2]]
            target = program[position+3]
            if program[position] == 99:
                # halt!
                break
            elif program[position] == 1:
                val = sum([op1,op2])
            elif program[position] == 2:
                val = op1 * op2
            else:
                # panic!
                print("panic!")
                exit(1)

            if target == 0:
               print(val)
            program[target] = val
            position = position + 4

        print(program[0])
        if program[0] == desired_output:
            print('whoohoo', noun, verb)
            print(noun * 100 + verb)
            exit(0)

# print(program)
# print()
