#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    p1, p2 = open("input").read().split("\n\n")
    p1 = [int(n) for n in p1.strip().split("\n")[1:]]
    p2 = [int(n) for n in p2.strip().split("\n")[1:]]
    return (p1, p2)

def play(d1, d2):
    n = 1
    while d1 and d2:
        #print(n, d1)
        #print(n, d2)
        c1, c2 = d1.pop(0), d2.pop(0)
        #print(c1, c2)
        #print()
        if c1 > c2:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
        n += 1
    if d1: 
        return d1
    else:
        return d2

def main():
    p1, p2 = read_input()
    winner = play(p1, p2)
    print(sum((i + 1) * c for (i, c) in enumerate(reversed(winner))))

if __name__ == '__main__':
    main()
