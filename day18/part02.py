#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def get_input():
    f = open("input")
    return [l.strip() for l in f]


def tokenize(expr):
    return re.findall(r'\d+|\(|\)|\*|\+', expr)

def parenthesize(tokens):
    indices = [i for i, op in enumerate(tokens) if op == '+']
    for i in indices:
        tokens[i - 1], tokens[i + 1] = '(' + tokens[i - 1], tokens[i + 1] + ')'
    return tokens

def ev(tokens, index):
    l = []
    while index < len(tokens) and tokens[index] != ')':
        if tokens[index] == '(':
            tokenl, nindex = ev(tokens, index + 1)
            l.append('(' + ' '.join(parenthesize(tokenl)) + ')')
            index = nindex + 1
        else:
            l.append(tokens[index])
            index += 1
    return l, index

def evaluate(ex):
    tokens = tokenize(ex)
    ast, ix = ev(tokens, 0)
    result = parenthesize(ast)
    return(eval(' '.join(result)))

def main():
    exprs = get_input()
    s = 0        
    for expr in exprs:
        s += evaluate(expr)
    print(s)
if __name__ == '__main__':
    main()
