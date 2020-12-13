#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
from enum import Enum

class Direction(Enum):
    North = 0
    East = 1
    South = 2
    West = 3
    Right = 4
    Left = 5
    Forward = 6

Instruction = namedtuple('Instruction', ['direction', 'arg'])

def read_input():
    m = { "N" : Direction.North,
      "E": Direction.East,
      "W": Direction.West,
      "S": Direction.South,
      "R": Direction.Right,
      "L": Direction.Left,
      "F": Direction.Forward,
     }

    instructions = []
    for l in open("input"):
        d, a = l.strip()[0], l.strip()[1:]        
        instructions.append(Instruction(m[d], int(a)))
    return instructions

def new_direction(current, instr):
    if instr.direction == Direction.Left:
        steps = - instr.arg // 90
    else:
        steps = instr.arg // 90
    return Direction((current.value + steps) % 4)

def make_absolute(current, forward):
    return Instruction(current, forward.arg)

def process(inp):
    direction = Direction.East
    x, y, = 0, 0
    for instr in inp:
        if instr.direction in [Direction.Left, Direction.Right]:
            direction = new_direction(direction, instr)
            continue
        if instr.direction == Direction.Forward:
            instr = make_absolute(direction, instr)
        if instr.direction == Direction.North:
            y += instr.arg
        elif instr.direction == Direction.South:
            y -= instr.arg
        elif instr.direction == Direction.West:
            x -= instr.arg
        elif instr.direction == Direction.East:
            x += instr.arg
    return (x, y)
def main():
    inp = read_input()
    (x, y) = process(inp)
    print(abs(x) + abs(y))

if __name__ == '__main__':
    main()
