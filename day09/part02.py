#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

def read_input():
    return [int(l.strip()) for l in open("input")]

def find_sequence(inp, n):
    partial_sums = list(itertools.accumulate(inp))
    for sum_start in range(len(inp)):
        for sum_end in range(sum_start + 1, len(inp)):
            if partial_sums[sum_end] - partial_sums[sum_start] == n:
                r = inp[sum_start+1:sum_end+1]
                return (max(r) + min(r))
def main():
    inp = read_input()
    print(find_sequence(inp, 10884537))

if __name__ == '__main__':
    main()
