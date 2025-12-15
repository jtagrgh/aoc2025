with open('day12.in') as file:
    lines = [x.strip() for x in file.readlines()]

shapes = []

for i,line in enumerate(lines):
    if len(line) >= 2 and line[1] == ':':
        shapes.append(lines[i+1:i+1+3])

counts = [''.join(shape).count('#') for shape in shapes]

trees = lines[30:]


def part1():
    valid_trees = 0

    for tree_str in trees:
        dim, quants = tree_str.split(': ')
        width, length = map(int, dim.split('x'))
        quants = list(map(int, quants.split(' ')))

        space_needed = sum(quant*counts[i] for i,quant in enumerate(quants))
        total_space = width * length

        if space_needed <= total_space - 100:
            valid_trees += 1

    print(valid_trees)


part1()