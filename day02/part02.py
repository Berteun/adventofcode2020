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
    i1 = pass_struct["lower"]
    i2 = pass_struct["upper"]
    password = pass_struct["password"]
    letter = pass_struct["letter"]
    return 1 == (password[i1 - 1] == letter) + (password[i2 - 1] == letter)

def main():
    inputs = read_input()
    print(sum(valid(pass_struct) for pass_struct in inputs))

if __name__ == '__main__':
    main()
