from collections import defaultdict
from functools import cache


with open('day11.in') as file:
    lines = [x.strip() for x in file.readlines()]

graph = defaultdict(list)

for line in lines:
    childs = line.split(' ')[1:]
    node = line[:3]
    graph[node].extend(childs)


def part1():

    @cache
    def dp(node): # Number of paths from node to 'out'
        if node == 'out':
            return 1
        return sum(dp(child) for child in graph[node])

    print(dp('you'))


def part2():

    @cache
    def dp(node, fft, dac):
        if node == 'out' and fft and dac:
            return 1
        fft |= node == 'fft'
        dac |= node == 'dac'
        return sum(dp(child, fft, dac) for child in graph[node])

    print(dp('svr', False, False))


part1()
part2()