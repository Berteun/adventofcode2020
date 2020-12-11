#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return [int(l.strip()) for l in open("input")]

cache = {}
def count_arrangements(inp, n):
    global cache
    if n == len(inp) - 1:
        return 1
    if n in cache:
        return cache[n]
    start = n
    arr = 0
    nxt = start + 1
    while nxt < len(inp):
        if inp[nxt] - inp[start] <= 3:
            arr += count_arrangements(inp, nxt)
        else:
            break
        nxt = nxt + 1
    cache[n] = arr
    return arr

def main():
    inp = read_input()
    inp.sort()
    inp = [0] + inp + [inp[-1] + 3]
    arr = count_arrangements(inp, 0)
    print(arr)

if __name__ == '__main__':
    main()
