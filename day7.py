from functools import cache


with open('day7.in') as file:
    grid = [list(x.strip()) for x in file.readlines()]

m,n = len(grid), len(grid[0])
s_xpos = grid[0].index('S')


def part1():
    vis = set()

    def total(y,x):
        if (y,x) in vis:
            return 0
        vis.add((y,x))
        if y > m-1:
            return 0
        if grid[y][x] == '^':
            return 1 + total(y, x-1) + total(y, x+1)
        return total(y+1, x)
    
    grand_total = total(0, s_xpos)
    print(grand_total)


def part2():

    @cache
    def total(y,x):
        if y > m-1:
            return 1
        if grid[y][x] == '^':
            return total(y, x-1) + total(y, x+1)
        return total(y+1, x)
    
    grand_total = total(0, s_xpos)
    print(grand_total)


part1()
part2()