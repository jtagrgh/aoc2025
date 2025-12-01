with open('day1.in', 'r') as file:
    lines = file.readlines()


def part1():
    n_times_0 = 0
    pos = 50
    for line in lines:
        dir = line[0]
        steps = int(line[1:]) * (1 if dir == 'R' else -1)
        pos = (pos + steps) % 100
        if pos == 0:
            n_times_0 += 1
        
    return n_times_0


def part2():
    n_times_0 = 0
    pos = 50
    for line in lines:
        dir = line[0]
        steps = int(line[1:])
        if dir == 'R':
            pos += steps
            n_times_0 += pos // 100
            pos %= 100
        else:
            n_times_0 += steps // 100
            steps %= 100
            if pos - steps <= 0 and pos != 0:
                n_times_0 += 1
            pos = (pos - steps) % 100

    return n_times_0
    

print(part1())
print(part2())