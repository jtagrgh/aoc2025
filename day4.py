with open ('day4.in', 'r') as file:
    grid = [list(line.strip()) for line in file.readlines()]

m,n = len(grid), len(grid[0])


def part1():
    total = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] != '@': 
                continue

            count = 0
            count += i > 0 and j > 0 and grid[i-1][j-1] == '@'
            count += i > 0 and grid[i-1][j] == '@'
            count += i > 0 and j < n-1 and grid[i-1][j+1] == '@'
            count += j < n-1 and grid[i][j+1] == '@'
            count += i < m-1 and j < n-1 and grid[i+1][j+1] == '@'
            count += i < m-1 and grid[i+1][j] == '@'
            count += i < m-1 and j > 0 and grid[i+1][j-1] == '@'
            count += j > 0 and grid[i][j-1] == '@'

            total += count < 4

    print(total)


def part2():
    changed = True
    total = 0

    while changed:
        changed = False

        for i in range(m):
            for j in range(n):
                if grid[i][j] != '@': 
                    continue

                count = 0
                count += i > 0 and j > 0 and grid[i-1][j-1] == '@'
                count += i > 0 and grid[i-1][j] == '@'
                count += i > 0 and j < n-1 and grid[i-1][j+1] == '@'
                count += j < n-1 and grid[i][j+1] == '@'
                count += i < m-1 and j < n-1 and grid[i+1][j+1] == '@'
                count += i < m-1 and grid[i+1][j] == '@'
                count += i < m-1 and j > 0 and grid[i+1][j-1] == '@'
                count += j > 0 and grid[i][j-1] == '@'

                if count < 4:
                    total += 1
                    grid[i][j] = '.'
                    changed = True

    print(total)


part1()
part2()
