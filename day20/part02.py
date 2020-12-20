#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from collections import defaultdict

def read_input():
    f = open("input")
    raw_tiles = f.read().strip().split("\n\n")    
    tiles = {}
    for tile in raw_tiles:
        lines = tile.strip().split("\n")
        number = int(lines[0][5:-1])
        tiles[number] = lines[1:]
    return tiles

def get_signature(edge):
    zero_one = edge.replace('#', '1').replace('.', '0')
    return int(zero_one, 2)

def get_signatures(edge):
    return [get_signature(edge), get_signature(edge[::-1])]

def print_tile(tile):
    print("\n".join(tile))

def get_left_edge(t):
    return ''.join([r[0] for r in t])

def get_bottom_edge(t):
    return t[-1][:]

def get_right_edge(t):
    return ''.join([r[-1] for r in t])

def get_top_edge(t):
    return t[0][:]

def get_edge_signatures(t):
    left = get_left_edge(t)
    bottom = get_bottom_edge(t)
    right = get_right_edge(t)
    top = get_top_edge(t)
    signatures = []
    for edge in [top, bottom, left, right]:
        signatures.extend(get_signatures(edge))
    return signatures

def process(tiles):
    count = defaultdict(list)
    for (tile_n, lines) in tiles.items():
        signatures = get_edge_signatures(lines)
        for s in signatures:
            count[s].append(tile_n)
    corners = []
    for (tile_n, lines) in tiles.items():
        signatures = get_edge_signatures(lines)
        edges = sum(len(count[s]) == 1 for s in signatures)
        # Cornes have two edges without neighbours, each edge has 2 signatures (normal and flipped)
        if (edges == 4):
            corners.append(tile_n)
    return corners, count

def make_start_tile(tile, edge_matches):
    tile.reverse()
    signatures = get_edge_signatures(tile)
    top, left = signatures[0], signatures[4]
    #print("Rotating")
    #print_tile(tile)
    #print("--")
    while len(edge_matches[top]) != 1 or len(edge_matches[left]) != 1:
        #print("rotating", edge_matches[top], edge_matches[left])
        tile = rotate_tile(tile)
        #print_tile(tile)
        #print("--")
        signatures = get_edge_signatures(tile)
        top, left = signatures[0], signatures[4]
    #print("done", edge_matches[signatures[0]], edge_matches[signatures[4]])
    return tile

def rotate_tile(tile):
    return list(''.join(l) for l in zip(*tile[::-1]))

def orient_left_matches(signature, tile):
    signatures = get_edge_signatures(tile)
    index = signatures.index(signature)
    if index // 2 == 0:
        rotations = 3
    if index // 2 == 1:
        rotations = 1
    if index // 2 == 2:
        rotations = 0
    if index // 2 == 3:
        rotations = 2
    for _ in range(rotations):
        tile = rotate_tile(tile)
    flip = get_signature(get_left_edge(tile)) != signature
    if flip:
        tile.reverse()
    return tile    

def orient_top_matches(signature, tile):
    tile = orient_left_matches(signature, tile)
    # Rotate 1 more time to bring to top
    tile = rotate_tile(tile)
    flip = get_signature(get_top_edge(tile)) != signature
    if flip:
        tile = [r[::-1] for r in tile]
    return tile    

def align(corners, tiles, edge_matches, total):
    # We can just assume the first corner is top-left. We can always flip and
    # orient everything we want.
    processed = 1
    current = corners[0]
    start_of_last_row = current
    #print("Placing", current, "top left")
    tiles[current] = make_start_tile(tiles[current], edge_matches)
    #print_tile(tiles[current])
    matrix = [ [tiles[current]] ]
    while processed < total:
        #print("current is ", current)
        right = get_signature(''.join([r[-1] for r in tiles[current]]))
        if len(edge_matches[right]) == 2:
            other_tiles = edge_matches[right]
            other_tile = [t for t in other_tiles if t != current][0]
            tiles[other_tile] = orient_left_matches(right, tiles[other_tile])
            matrix[-1].append(tiles[other_tile])
            #print("Placing", other_tile, "right of", current)
        else:
            # Extend to the bottom
            bottom = get_signature(matrix[-1][0][-1])
            other_tiles = edge_matches[bottom]
            other_tile = [t for t in other_tiles if t != start_of_last_row][0]
            #print("Placing", other_tile, "at start of new row")
            tiles[other_tile] = orient_top_matches(bottom, tiles[other_tile])
            #print("b", matrix[-1][0][-1], "\nt", tiles[other_tile][0])
            #print_tile(tiles[other_tile])
            matrix.append([])
            matrix[-1].append(tiles[other_tile])
            start_of_last_row = other_tile
        processed += 1
        current = other_tile
    return matrix

def print_matrix(matrix):
    for row in matrix:
        for n in range(len(row[0])):
            print("".join(t[n] for t in row))

def make_image(matrix):
    image = []
    for row in matrix:
        for n in range(len(row[0]) - 2):
            image.append("".join(t[n+1][1:-1] for t in row))
    return(image)

mon1s = "..................#."
mon2s = "#....##....##....###"
mon3s = ".#..#..#..#..#..#..."
mlen = len(mon1s)
mon1 = re.compile(mon1s)
mon2 = re.compile(mon2s)
mon3 = re.compile(mon3s)

def print_image(image):
    print("\n".join(image))


def count_monsters(image):
    matches = 0
    for y in range(len(image) - 2):
        for x in range(len(image[y]) - mlen):
            if (mon1.match(image[y][x:x + mlen])
                and mon2.match(image[y+1][x:x + mlen])
                    and mon3.match(image[y+2][x:x + mlen])):
                matches += 1
    return matches

def find_monsters(image):
    for m in range(2):
        for n in range(4):
            monsters = count_monsters(image)
            if monsters > 0:
                return(monsters)
            image = rotate_tile(image)
        image.reverse()

def compute_roughness(image, monsters):
    return ''.join(image).count('#') - monsters * ((mon1s + mon2s + mon3s).count('#'))

def main():
    tiles = read_input()
    corners,edge_matches = process(tiles)
    matrix = align(corners, tiles, edge_matches, len(tiles))
    image = make_image(matrix)
    monsters = find_monsters(image)
    roughness = compute_roughness(image, monsters)
    print("Found {} monsters. Roughness: {}".format(monsters, roughness))

    
if __name__ == '__main__':
    main()
