#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

def read_input():
    f = open("input")
    return [int(l.strip()) for l in f]

def process(inp, preamble=25):
    previous = []
    all_seen = defaultdict(int)
    for n in range(len(inp)):
        sums = []
        if n >= preamble:
            if inp[n] not in all_seen:
                return inp[n] 
            old = previous.pop(0)

            for (_, psums) in previous:
                osum = psums.pop(0)
                all_seen[osum] -= 1
                if all_seen[osum] == 0:
                    del all_seen[osum]
                
        for (v, _) in previous:        
            sums.append(v + inp[n])
            all_seen[v + inp[n]] += 1
        previous.append((inp[n], sums))

    return previous

def main():
    inp = read_input()
    print(process(inp))

if __name__ == '__main__':
    main()
