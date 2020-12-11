#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    return [int(l.strip()) for l in open("input")]

def find_differences(inp):
    diffs = []
    for n in range(len(inp)-1):
        diffs.append(inp[n+1]-inp[n])
    return diffs

def main():
    inp = read_input()
    inp.sort()
    inp = [0] + inp + [inp[-1] + 3]
    print(inp)
    diffs = find_differences(inp)
    print(diffs.count(1), diffs.count(3), diffs.count(1) * diffs.count(3)) 

if __name__ == '__main__':
    main()
