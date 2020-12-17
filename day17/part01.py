#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict

def read_input():
    f = open("input")
    sparse = defaultdict(lambda: ".")
    matrix = [list(l.strip()) for l in f]
    for (y,row) in enumerate(matrix):
        for (x,state) in enumerate(row):
            sparse[(x,y,0)] = state
    return sparse


def get_active_neighbours(inp, x, y, z):
    active = 0
    for dz in [-1,0,1]:
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dx == dy == dz == 0:
                    continue
                active += (inp[x+dx,y+dy,z+dz] == '#')
    return active

def evolve(inp, xl, xh, yl, yh, zl, zh):
    outp = defaultdict(lambda: ".")
    nbs = defaultdict(int)
    for z in range(zl, zh + 1):
        for y in range(yl, yh + 1):
            for x in range(xl, xh + 1):
                act = get_active_neighbours(inp, x, y, z)
                nbs[x,y,z] = act
                if inp[x,y,z] == '.' and act == 3: 
                    outp[x,y,z] = '#'
                elif inp[x,y,z] == '#' and 2 <= act <= 3:
                    outp[x,y,z] = '#'
                else:
                    outp[x,y,z] = '.'
    return outp, nbs

def print_field(inp, nbs, xl, xh, yl, yh, zl, zh):
    for z in range(zl, zh + 1):
        for y in range(yl, yh + 1):
            for x in range(xl, xh + 1):
                sys.stdout.write(inp[x,y,z])
            sys.stdout.write("    ")
            for x in range(xl, xh + 1):
                sys.stdout.write("{:02d} ".format(nbs[x,y,z]))
            sys.stdout.write("\n")
        sys.stdout.write("\n")

def main():
    inp = read_input()
    for n in range(6):     
        inp, nbs = evolve(inp, -1 - n, 9 + n, -1 - n, 9 + n, -1 - n, 1 + n)
        print_field(inp, nbs, -1 - n, 9 + n, -1 - n, 9 + n, -1 - n, 1 + n)

    print(sum(v == '#' for v in inp.values()))

if __name__ == '__main__':
    main()

