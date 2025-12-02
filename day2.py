with open('day2.in', 'r') as file:
    line = file.readline()

ranges = [tuple(map(int, pair.split('-'))) for pair in line.split(',')]


def part1():
    total = 0

    for start, end in ranges:
        for num in range(start, end+1):
            num_str = str(num)
            if len(num_str) % 2 != 0:
                continue
            mid = len(num_str) // 2
            if num_str[:mid] == num_str[mid:]:
                total += num

    print(total)


def part2():
    total = 0

    for start, end in ranges:
        for num in range(start, end+1):
            num_str = str(num)
            str_len = len(num_str)
            for i in range(1, len(num_str)):
                if str_len % i != 0:
                    continue
                if num_str == num_str[:i] * (str_len // i):
                    total += num
                    break

    print(total)


part1()
part2()