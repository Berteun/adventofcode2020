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

def is_valid(ticket, valid_numbers):
    return all(n in valid_numbers for n in ticket)

def filter_valid_tickets(validators, other_tickets):
    valid_numbers = set()
    for (rangea, rangeb) in validators.values():
        valid_numbers.update(range(rangea[0], rangea[1] + 1))
        valid_numbers.update(range(rangeb[0], rangeb[1] + 1))
    return [t for t in other_tickets if is_valid(t, valid_numbers)]

def unsolved(possible):
    return any(len(p) > 1 for p in possible)

def valid(validator, ticket_cat):
    return (validator[0][0] <= ticket_cat <= validator[0][1] or validator[1][0] <= ticket_cat <= validator[1][1])

def solve(validators, valid_tickets):
    possible = [set(validators.keys()) for _ in validators]
    while unsolved(possible):
        for n in range(len(possible)):
            for t in valid_tickets:
                for p in possible[n]:
                    if not valid(validators[p], t[n]):
                        possible[n].discard(p)
                        break
        for n in range(len(possible)):
            if len(possible[n]) == 1:
                for m in range(len(possible)):
                    if m == n:
                        continue
                    possible[m].difference_update(possible[n])
    return [p.pop() for p in possible]

def main():
    validators, my_ticket, other_tickets = read_input()
    valid_tickets = filter_valid_tickets(validators, other_tickets)
    solved = solve(validators, valid_tickets)
    sol = 1
    for (i,c) in enumerate(solved):
        if c.startswith('departure'):
            sol *= my_ticket[i]
    print(sol)

if __name__ == '__main__':
    main()
