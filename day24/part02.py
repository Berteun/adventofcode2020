#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

class Triple:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Triple(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Triple(self.x - other.x, self.y - other.y, self.z - other.z)

    def __abs__(self):
        return (abs(self.x) + abs(self.y) + abs(self.z))//2

    def __str__(self):
        return '({},{},{})'.format(self.x, self.y, self.z)

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

def split_line(l):
    i = 0
    tokens = []
    while i < len(l):
        if l[i] == 's' or l[i] == 'n':
            tokens.append(''.join(l[i:i+2]))
            i += 2
        else:
            tokens += l[i]
            i += 1
    return tokens

def read_input():
    inp = []
    for l in open("input"):
        l = l.strip()
        inp.append(split_line(l))
    return inp


m = {
    # First axis
    "nw": Triple( 0,-1, 1),
    "se": Triple( 0, 1,-1),
    # Second axis
    "ne": Triple( 1,-1, 0),
    "sw": Triple(-1, 1, 0),
    # Thirds axis
    "w":  Triple(-1, 0, 1),
    "e":  Triple( 1, 0,-1),
}

def map_to_coord(inp):
    return m[inp]

def walk(inp):
    coord = Triple()
    for i in inp:
        coord = coord + map_to_coord(i)
    return coord

def neighbours(tile):
    return { tile + n for n in m.values()}

def tile_list(tiles):
    all_tiles = set()
    for tile in tiles:
        all_tiles.add(tile)
        all_tiles.update(neighbours(tile))
    return all_tiles

def evolve(tiles):
    active_tiles = tile_list(tiles)
    new_tiles = defaultdict(int)
    for tile in active_tiles:
        c = sum(tiles[n] for n in neighbours(tile))
        if tiles[tile] == 1:
            if 0 < c <= 2:
                new_tiles[tile] = 1
            else:
                new_tiles[tile] = 0
        else:
            if c == 2:
                new_tiles[tile] = 1
            else:
                new_tiles[tile] = 0
    return new_tiles

def main():
    tiles = defaultdict(int)
    lines = read_input()    
    for l in lines:
        final = walk(l)
        tiles[final] = 1 - tiles[final]
    print('Day 0', sum(v for v in tiles.values()))
    for n in range(100):
        tiles = evolve(tiles)
        print('Day {}'.format(n + 1), sum(v for v in tiles.values()))

if __name__ == '__main__':
    main()
