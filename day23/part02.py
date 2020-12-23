#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return list(int(n) for n in open("input").readline().strip())

def extend_input(inp):
    for n in range(len(inp) + 1, 1_000_001):
        inp.append(n)
    return inp

def make_array(inp):
    inp = [i - 1 for i in inp]
    nbs = [0] * len(inp)
    for i, n in enumerate(inp):
        nbs[n] = inp[(i + 1) % len(inp)]
    return inp[0], nbs

def remove_3(nbs, current):
    start = current
    removed = []
    for _ in range(3):
        current = nbs[current]
        removed.append(current)
    current = nbs[current]
    nbs[start] = current
    return removed

def insert_3(nbs, dest, removed):
    old = nbs[dest]
    nbs[dest] = removed[0]
    nbs[removed[-1]] = old

def select_dest(nbs, current, removed):
    dest = (current - 1) % len(nbs)
    while dest in removed:
        dest = (dest - 1) % len(nbs)
    return dest

def do_moves(nbs, current):
    removed = remove_3(nbs, current)
    dest = select_dest(nbs, current, removed)
    insert_3(nbs, dest, removed)
    current = nbs[current]
    return current

def print_solution(nbs):
    nb1 = nbs[0]
    nb2 = nbs[nb1]
    print("solution: {}".format((nb1 + 1) * (nb2 + 1)))

def main():
    inp = read_input()
    inp = extend_input(inp)
    current, nbs = make_array(inp)
    for n in range(10_000_000):
        current = do_moves(nbs, current)
    print_solution(nbs)

if __name__ == '__main__':
    main()
