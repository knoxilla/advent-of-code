#!/usr/bin/env python

import sys
import os
from pprint import pprint as pp

position = { 'x': 0, 'y': 0, 'pointed': 'N'}

steps = ['R4','R3','L3','L2','L1','R1','L1','R2','R3','L5','L5','R4','L4','R2','R4','L3','R3','L3','R3','R4','R2','L1','R2','L3','L2','L1','R3','R5','L1','L4','R2','L4','R3','R1','R2','L5','R2','L189','R5','L5','R52','R3','L1','R4','R5','R1','R4','L1','L3','R2','L2','L3','R4','R3','L2','L5','R4','R5','L2','R2','L1','L3','R3','L4','R4','R5','L1','L1','R3','L5','L2','R76','R2','R2','L1','L3','R189','L3','L4','L1','L3','R5','R4','L1','R1','L1','L1','R2','L4','R2','L5','L5','L5','R2','L4','L5','R4','R4','R5','L5','R3','L1','L3','L1','L1','L3','L4','R5','L3','R5','R3','R3','L5','L5','R3','R4','L3','R3','R1','R3','R2','R2','L1','R1','L3','L3','L3','L1','R2','L1','R4','R4','L1','L1','R3','R3','R4','R1','L5','L2','R2','R3','R2','L3','R4','L5','R1','R4','R5','R4','L4','R1','L3','R1','R3','L2','L3','R1','L2','R3','L3','L1','L3','R4','L4','L5','R3','R5','R4','R1','L2','R3','R5','L5','L4','L1','L1']

def turn(way):
	global position
	turn_map = {('N','R'): 'E',
							('N','L'): 'W',
							('S','R'): 'W',
							('S','L'): 'E',
							('W','R'): 'N',
							('W','L'): 'S',
							('E','R'): 'S',
							('E','L'): 'N'}
	position['pointed'] = turn_map[(position['pointed'],way)]

turn('R')
print(position)
turn('R')
print(position)
turn('R')
print(position)
turn('R')
print(position)

def move(how_many):
	global position
	switcher = {
		'N': lambda position: position['y'] += how_many,
		'S': lambda position: position['y'] -= how_many,
		'W': lambda position: position['x'] += how_many,
		'E': lambda position: position['x'] -= how_many,
	}
	move_it = switcher.get(position['pointed', lambda: "nothing")
	move_it()



