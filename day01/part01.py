#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_input():
    f = open('input')
    return [int(l) for l in f]

def find_2020_sum(sorted_costs):
    left = 0
    right = len(sorted_costs) - 1
    while left < right and sorted_costs[left] + sorted_costs[right] != 2020:
        s = sorted_costs[left] + sorted_costs[right]
        if (s < 2020):
            left += 1
        if (s > 2020):
            right -= 1
    return sorted_costs[left], sorted_costs[right]

def main():
    costs = read_input()
    costs.sort()
    p, q = find_2020_sum(costs)
    print(p * q)

if __name__ == '__main__':
    main()
