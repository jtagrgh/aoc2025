from math import prod


with open('day6.in', 'r') as file:
    lines = file.readlines()

cols = list(zip(*[[x for x in line.split()] for line in lines]))


def part1():
    total = 0
    for col in cols:
        if col[-1] == '*':
            total += prod(map(int, col[:-1]))
        elif col[-1] == '+':
            total += sum(map(int, col[:-1]))
    
    print(total)


def part2():
    cols = list(zip(*lines))
    ops = [[]]
    for col in cols:
        if all(x == ' ' for x in col):
            ops.append([])
        else:
            if col[-1] in ('+', '*'):
                ops[-1].append(col[-1])
            ops[-1].append(int(''.join(x for x in col[:-1] if x != ' ')))
    
    total = 0
    for op in ops:
        total += prod(op[1:]) if op[0] == '*' else sum(op[1:])

    print(total)


part1()
part2()