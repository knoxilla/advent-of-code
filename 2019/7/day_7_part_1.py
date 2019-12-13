#!/usr/bin/env python3

from itertools import permutations
import logging
import math
import sys


logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger('intcode')

input_file = open(sys.argv[1], "r")
raw  = input_file.readline().split(",")
input_file.close()

##### Part 1
# Max thruster signal 43210 (from phase setting sequence 4,3,2,1,0):
test1 = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0".split(",")

# # Max thruster signal 54321 (from phase setting sequence 0,1,2,3,4):
test2 = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0".split(",")

# # Max thruster signal 65210 (from phase setting sequence 1,0,4,3,2):
test3 = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0".split(",")

phases = [0,1,2,3,4]

##### Part 2
# Max thruster signal 139629729 (from phase setting sequence 9,8,7,6,5):
# test1 = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5".split(",")

# Max thruster signal 18216 (from phase setting sequence 9,7,8,5,6):
# test2="3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10".split(",")

# phases = [5,6,7,8,9]

initial_program = [ int(r) for r in test1 ]

perms = permutations(phases)

# initial_input = int(input("Enter input: "))
initial_input = 0

program = list(initial_program)

def get_par(inst, par, modes):
    if modes[par-1] == 0:
       thing = program[inst[par]]
    else:
       thing = inst[par]
    return thing

def run_program(passed_inputs):
    inputs = passed_inputs # [passed_inputs[0]]
    input_idx = 0
    position = 0
    outputs = []
    steps = 0
    while True:
        steps = steps + 1
        jumping = False
        rawcode = program[position]
        padded_code = f'{rawcode:05}'
        opcode = int(padded_code[3:5])
        modes = list(reversed([ int(m) for m in padded_code[0:3] ]))
        # logger.error(f"{padded_code} {opcode} {modes}")
        if opcode not in [1,2,3,4,5,6,7,8,99]:
            logger.info('panic')
            exit(1)
        if opcode == 99:
            logger.info('halt')
            # print()
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
            logger.error("what the heck...")
            exit(1)

        # logger.info(f"  {opcode} {position} {steps} {inst} {targ_addr}")

        if opcode == 1: # update target with parameter sum
            val = par1 + par2
            logger.info(f'   sum:   {par1}+{par2}={val} to pos {targ_addr}')
            program[targ_addr] = val
        elif opcode == 2:  # update target with parameter product
            val = par1 * par2
            logger.info(f'   prod:  {par1}*{par2}={val} to pos {targ_addr}')
            program[targ_addr] = val
        elif opcode == 3: # update or insert
            val = inputs[input_idx]
            input_idx = input_idx + 1
            logger.error(f'   input: {val} to pos {targ_addr}')
            # program[targ_addr:targ_addr] = val
            program[targ_addr] = val
        elif opcode == 4: # output
            val = par1
            logger.info(f'   output: {val}')
            outputs.append(val)
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

    return(outputs[-1])


best_result = 0
results = 0
best_perm = None

for perm in perms:
    logger.error(f" PERM:        {perm}")
    inp = 0
    for idx, phase in enumerate(perm):
        program = list(initial_program)
        logger.info(f" PHASE:       {phase}")
        logger.info(f" AMPLIFER:    {'ABCDE'[idx]}")
        logger.info(f" INPUT:       {inp}")
        results = run_program([phase,inp])
        inp = results
    print(program)
    logger.error(f' {best_result} {results}')
    if results > best_result:
        best_result = results
        best_perm = perm

print()
print(best_result)
print(best_perm)

