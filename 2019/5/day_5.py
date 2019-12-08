#!/usr/bin/env python3

import math
import sys

input_file = open(sys.argv[1], "r")
raw  = input_file.readline().split(",")
input_file.close()

# test1 = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9".split(",")
# test2 = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1".split(",")
# test3 = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99".split(",")

initial_program = [ int(r) for r in raw ]

initial_input = int(input("Enter input: "))

program = list(initial_program)
print(initial_program)
position = 0

def get_par(inst, par, modes):
    if modes[par-1] == 0:
       thing = program[inst[par]]
    else:
       thing = inst[par]
    return thing

inputs = initial_input
outputs = []
steps = 0
while True:
    steps = steps + 1
    jumping = False
    rawcode = program[position]
    padded_code = f'{rawcode:05}'
    opcode = int(padded_code[3:5])
    modes = list(reversed([ int(m) for m in padded_code[0:3] ]))
    print(padded_code, opcode, modes)
    if opcode not in [1,2,3,4,5,6,7,8,99]:
        print('panic')
        exit(1)
    if opcode == 99:
        print('halt')
        break

    if opcode in [1,2]:
        inst_width = 4
        inst = program[position:position+inst_width]
        par1 = get_par(inst, 1, modes) # program[program[position+1]]
        par2 = get_par(inst, 2, modes) # program[program[position+2]]
        par3 = inst[3]
        targ_addr = par3
    elif opcode == 3:
        inst_width = 2
        inst = program[position:position+inst_width]
        # par1 = get_par(inst, 1, modes)
        par1 = program[position+1]
        targ_addr = par1
    elif opcode == 4:
        inst_width = 2
        inst = program[position:position+inst_width]
        par1 = get_par(inst, 1, modes)
        # par1 = program[position+1]
        targ_addr = 'nil'
    elif opcode in [5,6]:
        inst_width = 3
        inst = program[position:position+inst_width]
        par1 = get_par(inst, 1, modes) # program[program[position+1]]
        par2 = get_par(inst, 2, modes) # program[program[position+2]]
        targ_addr = 'nil'
    elif opcode in [7,8]:
        inst_width = 4
        inst = program[position:position+inst_width]
        par1 = get_par(inst, 1, modes) # program[program[position+1]]
        par2 = get_par(inst, 2, modes) # program[program[position+2]]
        par3 = inst[3]
        targ_addr = par3
    else:
        print("what the heck...")
        exit(1)

    print("  ", opcode, position, steps, inst, targ_addr)

    if opcode == 1:
        val = par1 + par2
        print(f'   sum: {par1}+{par2}={val} to pos {targ_addr}')
        program[targ_addr] = val
    elif opcode == 2:
        val = par1 * par2
        print(f'   prod: {par1}*{par2}={val} to pos {targ_addr}')
        program[targ_addr] = val
    elif opcode == 3:
        val = inputs
        print(f'   input: {val} to pos {targ_addr}')
        program[targ_addr] = val
    elif opcode == 4:
        val = par1
        print(f'   output: {val}')
        outputs.append(val)
        # if val != 0:
            # print(outputs)
            # exit(1)
    elif opcode == 5: # jump if true
        if par1 != 0:
            jumping = True
            position = par2
    elif opcode == 6: # jump if false
        if par1 == 0:
            jumping = True
            position = par2
    elif opcode == 7: # store if less then
        if par1 < par2:
            program[targ_addr] = 1
        else:
            program[targ_addr] = 0
    elif opcode == 8: # store if equals
        if par1 == par2:
            program[targ_addr] = 1
        else:
            program[targ_addr] = 0


    if not jumping:
        position = position + inst_width

#print(program[0:position+20])
print()
print(outputs)
print()

# print(program)
# print()
