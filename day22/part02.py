#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

def read_input():
    p1, p2 = open("input").read().split("\n\n")
    p1 = [int(n) for n in p1.strip().split("\n")[1:]]
    p2 = [int(n) for n in p2.strip().split("\n")[1:]]
    return (p1, p2)

def play(d1, d2, d=1):
    n = 1
    seen = set()
    while d1 and d2:
        key = (tuple(d1), tuple(d2))
        if key in seen:
            return 1, d1
        seen.add(key)
        #print("Player 1's deck: {}".format(",".join(str(i) for i in d1)))
        #print("Player 2's deck: {}".format(",".join(str(i) for i in d2)))
        c1, c2 = d1.popleft(), d2.popleft()
        #print("Player 1 plays:", c1)
        #print("Player 2 plays:", c2)

        if c1 <= len(d1) and c2 <= len(d2):
            #print("Playing a sub-game to determine the winner...")
            sub1 = list(d1)[:c1]
            sub2 = list(d2)[:c2]
            winner, _ = play(deque(sub1), deque(sub2), d + 1)
        else:
            winner = 1 if c1 > c2 else 2

        #print("Player {} wins round {} of game {}!".format(winner, n, d))

        if winner == 1:
            d1.append(c1)
            d1.append(c2)
        else:
            d2.append(c2)
            d2.append(c1)
        n += 1

    if d1: 
        return 1, d1
    else:
        return 2, d2

def main():
    p1, p2 = read_input()
    winner, deck = play(deque(p1), deque(p2))
    print(winner, deck)
    print(sum((i + 1) * c for (i, c) in enumerate(reversed(deck))))

if __name__ == '__main__':
    main()
