#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_input():
    f = open('input')
    return [int(l) for l in f]

def find_2020_helper(sorted_costs, goal, start_idx):
    left = start_idx + 1
    right = len(sorted_costs) - 1
    while left < right and sorted_costs[left] + sorted_costs[right] != goal:
        s = sorted_costs[left] + sorted_costs[right]
        if (s < goal):
            left += 1
        if (s > goal):
            right -= 1
    return sorted_costs[left], sorted_costs[right]

def find_2020_sum(sorted_costs):
    for (i, c) in enumerate(sorted_costs):
        p, q = find_2020_helper(sorted_costs, 2020 - c, i)
        if p + q == 2020 - c:
            return c, p, q

def main():
    costs = read_input()
    costs.sort()
    p, q, r = find_2020_sum(costs)
    print(p * q * r)

if __name__ == '__main__':
    main()
