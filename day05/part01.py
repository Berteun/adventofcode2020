#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_line(l):
    return int(l.replace('F', '0')
                .replace('B', '1')
                .replace('L', '0')
                .replace('R', '1'), 2);

def read_input():
    f = open('input')
    return [parse_line(l) for l in f]

def main():
    inputs = read_input()
    print(max(inputs))

if __name__ == '__main__':
    main()
