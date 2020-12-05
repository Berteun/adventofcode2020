#!/usr/bin/env python
# -*- coding: utf-8 -*-


def parse_line(l):
    lower_upper, letter, password = l.split(' ')
    lower, upper = lower_upper.split('-')
    return {
        "lower": int(lower),
        "upper": int(upper),
        "letter": letter[0],
        "password": password.strip(),
    }
def read_input():
    f = open('input')
    return [parse_line(l) for l in f]

def valid(pass_struct):
    return pass_struct["lower"] <= pass_struct["password"].count(pass_struct["letter"]) <= pass_struct["upper"];

def main():
    inputs = read_input()
    print(sum(valid(pass_struct) for pass_struct in inputs))

if __name__ == '__main__':
    main()
