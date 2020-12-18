#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def get_input():
    f = open("input")
    return [l.strip() for l in f]


def tokenize(expr):
    return re.findall(r'\d+|\(|\)|\*|\+', expr)

def flatten(tokens):
    result = int(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        if op == '+':
            result += int(tokens[i + 1])
        else:
            result *= int(tokens[i + 1])
        i += 2
    return result

def ev(tokens, index):
    l = []
    while index < len(tokens) and tokens[index] != ')':
        if tokens[index] == '(':
            tokenl, nindex = ev(tokens, index + 1)
            l.append(flatten(tokenl))
            assert(tokens[nindex] == ')')
            index = nindex + 1
        else:
            l.append(tokens[index])
            index += 1
    return l, index

def evaluate(ex):
    tokens = tokenize(ex)
    ast, ix = ev(tokens, 0)
    result = flatten(ast)
    return(result)

def main():
    exprs = get_input()
    s = 0        
    for expr in exprs:
        s += evaluate(expr)
    print(s)
if __name__ == '__main__':
    main()
