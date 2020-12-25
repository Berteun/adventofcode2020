#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open("input")
    #return [5764801, 17807724]
    return int(f.readline().strip()), int(f.readline().strip())

MOD = 20201227
def loop(subj, pub1, pub2):
    n = 0
    v = 1
    l1 = None
    l2 = None
    while True:
        n += 1
        v *= subj
        v %= MOD
        if v == pub1:
            l1 = n
        if v == pub2:
            l2 = n
        if l1 and l2:    
            return l1, l2

def main():
    sub = 7
    pub1, pub2 = read_input()
    l1, l2 = loop(sub, pub1, pub2)
    print(pow(pub1, l2, MOD))
    print(pow(pub2, l1, MOD))
    
if __name__ == '__main__':
    main()
