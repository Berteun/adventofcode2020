#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 3232
def intersect(group):
    items = [g for g in group.split('\n') if g]
    common = set(items[0])
    for g in items[1:]:
        common.intersection_update(set(g))
    return common

def read_input():
    inp = open('input').read()
    raw_groups = inp.split('\n\n')
    return [intersect(g) for g in raw_groups]

def main():
    groups = read_input()
    print(sum(len(g) for g in groups))

if __name__ == '__main__':
    main()
