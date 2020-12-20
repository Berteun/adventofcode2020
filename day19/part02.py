#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    rules = {}
    f = open("input")
    for l in f:
        if not l.strip():
            break
        rule_num, branche_str = l.strip().split(':')
        branches = [b.strip().split() for b in branche_str.split(' | ')]
        rules[int(rule_num)] = [[int(b) if b.isdigit() else eval(b) for b in bl] for bl in branches]

    strings = []
    for l in f:
        strings.append(l.strip())
    return rules, strings

def matches(s, s_i, rules, starting_rule):
    if s_i >= len(s):
        return False, s_i
    rule = rules[starting_rule]
    for branch in rule:
        n_i = s_i
        for subrule in branch:
            if isinstance(subrule, str):
                matched, n_i = s[s_i] == subrule, s_i + 1
            else:
                matched, n_i = matches(s, n_i, rules, subrule)
            if not matched:
                break
        if matched:
            return True, n_i
    return False, s_i

def main():
    rules, strings = read_input()
    matched = 0
    for s in strings:
        for (n,m) in [(n,m) for n in range(1, 10) for m in range(1, 10)]:
            rules[8] = [[42] * (n)]
            rules[11] = [[42] * (m) + [31] * (m)]
            match, processed = matches(s, 0, rules, 0)
            if (match):
                matched += (match and processed == len(s))
                break
    print(matched)

if __name__ == '__main__':
    main()
