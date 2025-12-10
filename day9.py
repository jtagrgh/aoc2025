from itertools import combinations, pairwise
import matplotlib.pyplot as plt


with open('day9.in') as file:
    lines = file.readlines()

tiles = [tuple(map(int, line.strip().split(','))) for line in lines]

rect_size = lambda a,b: abs((a[0] - b[0] + 1) * (a[1] - b[1] + 1))


def part1():
    max_area = max(rect_size(a,b) for a,b in combinations(tiles, 2))
    print(max_area)


def part2():
    # x_vals = [tile[0] for tile in tiles]
    # y_vals = [tile[1] for tile in tiles]
    # plt.plot(x_vals, y_vals)
    # plt.scatter(x_vals, y_vals, marker=',', s=2, c='r')

    horizontal_lines = []
    vertical_lines = []
    for a,b in pairwise(tiles + [tiles[0]]):
        a,b = sorted([a,b])
        if a[0] == b[0]:
            vertical_lines.append((a[0], a[1], b[1]))
        elif a[1] == b[1]:
            horizontal_lines.append((a[1], a[0], b[0]))

    top_midline, bottom_midline = sorted(horizontal_lines, key=lambda x: (x[2] - x[1], x[0]))[-2:]

    upper_endpoint = (top_midline[2], top_midline[0])

    lower_endpoint = (bottom_midline[2], bottom_midline[0])

    min_y = max((line for line in horizontal_lines if line[1] <= lower_endpoint[0] <= line[2] and line[0] < lower_endpoint[1]), key=lambda line: line[0])[0]

    max_y = min((line for line in horizontal_lines if line[1] <= upper_endpoint[0] <= line[2] and line[0] > upper_endpoint[1]), key=lambda line: line[0])[0]

    upper_otherpoints = [tile for tile in tiles if upper_endpoint[1] <= tile[1] <= max_y and tile[0] < upper_endpoint[0]]

    lower_otherpoints = [tile for tile in tiles if min_y <= tile[1] <= lower_endpoint[1] and tile[0] < lower_endpoint[0]]

    max_area = 0
    max_otherpoint = (0,0)

    for otherpoint in lower_otherpoints:
        width = abs(lower_endpoint[0] - otherpoint[0]) + 1
        height = abs(lower_endpoint[1] - otherpoint[1]) + 1
        area = width * height
        if area > max_area:
            max_otherpoint = otherpoint
        max_area = max(max_area, area)

    for otherpoint in upper_otherpoints:
        width = abs(upper_endpoint[0] - otherpoint[0]) + 1
        height = abs(otherpoint[1] - upper_endpoint[1]) + 1
        area = width * height
        if area > max_area:
            max_otherpoint = otherpoint
        max_area = max(max_area, area)

    print('max_area', max_area)

    # plt.scatter([max_otherpoint[0]], [max_otherpoint[1]], marker=',', c='r', s=4)

    # plt.plot([0, 100000], [max_y, max_y])
    # plt.plot([0, 100000], [min_y, min_y])

    # plt.show()


part1()
part2()