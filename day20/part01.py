#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

def read_input():
    f = open("input")
    raw_tiles = f.read().strip().split("\n\n")    
    tiles = []
    for tile in raw_tiles:
        lines = tile.strip().split("\n")
        number = int(lines[0][5:-1])
        tiles.append((number, lines[1:]))
    return tiles

def get_signatures(edge):
    zero_one = edge.replace('#', '1').replace('.', '0')
    return [int(zero_one, 2), int(zero_one[::-1], 2)]

def get_edge_signatures(t):
    top = t[0][:]
    bottom = t[-1][:]
    left = ''.join([r[0] for r in t])
    right = ''.join([r[-1] for r in t])
    signatures = []
    for edge in [top, bottom, left, right]:
        signatures.extend(get_signatures(edge))
    return signatures

def process(tiles):
    count = defaultdict(int)
    for (tile_n, lines) in tiles:
        signatures = get_edge_signatures(lines)
        for s in signatures:
            count[s] += 1
    p = 1
    for (tile_n, lines) in tiles:
        signatures = get_edge_signatures(lines)
        edges = sum(count[s] == 1 for s in signatures)
        # Cornes have two edges without neighbours, each edge has 2 signatures (normal and flipped)
        if (edges == 4):
            p *= tile_n
    return p

def main():
    tiles = read_input()
    p = process(tiles)
    print(p)

if __name__ == '__main__':
    main()
