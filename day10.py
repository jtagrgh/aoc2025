from collections import namedtuple, defaultdict
from itertools import combinations
import cvxpy as cp
import numpy as np


with open('day10.in') as file:
    lines = [x.split(' ') for x in file.readlines()]

Machine = namedtuple('Machine', ['lights', 'buttons', 'joltages'])

machines = []

for line in lines:
    light_str = line[0][1:-1]
    light_bin = []
    for c in light_str:
        light_bin.append(1 if c == '#' else 0)
    buttons = line[1:-1]
    buttons = [tuple(map(int, button[1:-1].split(','))) for button in buttons]
    joltage_str = line[-1].strip()[1:-1]
    joltages = tuple(map(int, joltage_str.split(',')))
    machines.append(Machine(light_bin, buttons, joltages))


def part1():
    total = 0

    for machine in machines:
        for n in range(1, len(machine.buttons)):
            done = False
            for sel in combinations(machine.buttons, n):
                lights = [0] * len(machine.lights)
                for button in sel:
                    for idx in button:
                        lights[idx] = not lights[idx]
                if lights == machine.lights:
                    done = True
                    total += n
                    break
            if done:
                break

    print(total)


def part2():
    total = 0

    for machine in machines:
        n = len(machine.buttons)
        m = len(machine.joltages)

        button_array = [np.zeros(n) for _ in range(m)]

        for i,button in enumerate(machine.buttons):
            for idx in button:
                button_array[idx][i] = 1

        x = cp.Variable(n, nonneg=True, integer=True) # Buttons
        y = cp.Variable(m, integer=True) # Joltages

        constraints = []

        for i,jolt in enumerate(machine.joltages):
            constraints += [y[i] == jolt]
            constraints += [y[i] == (x @ button_array[i])]

        problem = cp.Problem(cp.Minimize(cp.sum(x)), constraints)

        problem.solve(solver='SCIP')

        assert(x.value is not None)

        total += int(x.value.sum())

    print(total)


part1()
part2()