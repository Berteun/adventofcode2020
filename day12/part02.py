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

def new_waypoint(wx, wy, instr):
    if instr.direction == Direction.Left:
        steps = instr.arg // 90
    else:
        steps = -instr.arg // 90
    newD = (wx + wy*1j) * 1j**steps
    return int(newD.real), int(newD.imag)

def process(inp):
    direction = Direction.East
    x, y, = 0, 0
    wx, wy, = 10, 1

    for instr in inp:
        if instr.direction in [Direction.Left, Direction.Right]:
            (wx, wy) = new_waypoint(wx, wy, instr)
            continue
        if instr.direction == Direction.Forward:
            (x, y) = x + wx * instr.arg, y + wy * instr.arg
        if instr.direction == Direction.North:
            wy += instr.arg
        elif instr.direction == Direction.South:
            wy -= instr.arg
        elif instr.direction == Direction.West:
            wx -= instr.arg
        elif instr.direction == Direction.East:
            wx += instr.arg
    return (x, y)
def main():
    inp = read_input()
    (x, y) = process(inp)
    print(abs(x) + abs(y))

if __name__ == '__main__':
    main()
