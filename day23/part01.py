#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    #return [3,8,9,1,2,5,4,6,7]
    return list(int(n) for n in open("input").readline().strip())

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
    print("pick up: {}".format(', '.join(str(r + 1) for r in removed)))
    #print_cups(current, nbs)
    dest = select_dest(nbs, current, removed)
    print("destination: {}".format(dest + 1))
    insert_3(nbs, dest, removed)
    current = nbs[current]
    return current

def print_cups(current, nbs):
    start = current
    current = nbs[start]
    order = [start]
    while current != start:
        order.append(current)
        current = nbs[current]
    print("cups: {}".format(" ".join(str(o + 1) for o in order)))

def print_solution(nbs):
    current = nbs[0]
    order = []
    while current != 0:
        order.append(str(current + 1))
        current = nbs[current]
    print("solution: {}".format("".join(order)))

def main():
    inp = read_input()
    current, nbs = make_array(inp)
    print(inp)
    print(current, nbs)
    for n in range(100):
        print('-- move {} --'.format(n + 1))
        print_cups(current, nbs)
        current = do_moves(nbs, current)
        print();
    print("-- final --")
    print_cups(current, nbs)
    print_solution(nbs)

if __name__ == '__main__':
    main()
