#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pprint
import re
from collections import defaultdict

re_target = re.compile(r'([0-9]+) (\w+ \w+)* bag')
re_line = re.compile(r'(\w+ \w+) bags contain (([0-9]+) (\w+ \w+)* bags?(, ([0-9]+) (\w+ \w+) bags?)*\.|no other bags\.)')
def parse_line(l):
    graph = {}
    match = re_line.match(l)
    source = match[1]
    graph[source] = {}
    if "no other" not in match[2]:
        targets = re_target.findall(match[2])
        for (mult, target) in targets:
            graph[source][target] = int(mult)
    return graph

def read_input():
    graph = {}
    for l in open('input'):
        graph.update(parse_line(l.strip()))
    return graph

def count_bags(graph, source):
    count = 1
    if graph[source]:
        for (target, weight) in graph[source].items():
            count += weight * count_bags(graph, target)
    return count

def main():
    graph = read_input()
    c = count_bags(graph, 'shiny gold')
    print(c - 1)

if __name__ == '__main__':
    main()
