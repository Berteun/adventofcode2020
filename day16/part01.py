#!/usr/bin/env python
# -*- coding: utf-8 -*-

def parse_range(r):
    a, b = r.split("-")
    return (int(a), int(b))

def read_validators(f):
    l = f.readline().strip()
    validators = {}
    while l:
        name, ranges = l.split(": ")
        rangea_str, rangeb_str = ranges.split(" or ")
        range_a, range_b = parse_range(rangea_str), parse_range(rangeb_str)
        validators[name] = (range_a, range_b)
        l = f.readline().strip()
    return validators
        
def read_my_ticket(f):
    f.readline()
    return [int(x) for x in f.readline().strip().split(",")]

def read_other_tickets(f):
    tickets = []
    for l in f:
        if not l[0].isdigit():
            continue
        tickets.append([int(x) for x in l.strip().split(",")])
    return tickets

def read_input():
    f = open("input")
    validators = read_validators(f)
    my_ticket = read_my_ticket(f)
    other_tickets = read_other_tickets(f)
    return validators, my_ticket, other_tickets

def error_rate(validators, other_tickets):
    valid_numbers = set()
    for (rangea, rangeb) in validators.values():
        valid_numbers.update(range(rangea[0], rangea[1] + 1))
        valid_numbers.update(range(rangeb[0], rangeb[1] + 1))
    error_rate = 0
    for t in other_tickets:
        for n in t:
            if n not in valid_numbers:
                error_rate += n
    return error_rate

def main():
    validators, _, other_tickets = read_input()
    print(error_rate(validators, other_tickets))

if __name__ == '__main__':
    main()
