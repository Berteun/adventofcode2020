#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

def read_input():
    f = open('input')
    int(f.readline().strip())
    schedule_line = f.readline().strip()
    return [(-i % int(x), int(x)) for (i, x) in enumerate(schedule_line.split(",")) if x != "x"]

def find_earliest(*schedules):
    M = math.prod(m_i for (_,m_i) in schedules)
    s = 0
    # See: https://mathworld.wolfram.com/ChineseRemainderTheorem.html
    for (a_i,m_i) in schedules:
        b_i = pow(M//m_i,-1,m_i)
        s += a_i * b_i * (M//m_i)
    return s, M

def main():
    schedules = read_input()
    s, M = find_earliest(*schedules)
    print(s % M)

if __name__ == '__main__':
    main()
