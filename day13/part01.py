#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read_input():
    f = open('input')
    start_time = int(f.readline().strip())
    schedules = [int(x) for x in f.readline().strip().split(',') if x != "x"]
    return start_time, schedules

def find_earliest(start, schedules):
    departures = []
    for s in schedules:
        p, r = divmod(start, s)
        if r > 0:
            departures.append(((p + 1) * s, s))
        else:
            departures.append((p * s), s)# == start
    departure,schedule = min(departures)
    return (departure - start,schedule)

def main():
    start, schedules = read_input()
    waiting,s_id = find_earliest(start, schedules)
    print(waiting * s_id)

if __name__ == '__main__':
    main()
