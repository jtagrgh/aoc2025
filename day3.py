from itertools import combinations

with open('day3.in', 'r') as file:
    lines = [x.strip() for x in file.readlines()]


def part1():
    total = 0

    for bank in lines:
        max_joltage = max(combinations(bank, 2))
        total += int(''.join(max_joltage))

    print(total)


def part2():
    total = 0

    for bank in lines:
        count = len(bank)
        joltage = ''
        start_idx = 0
        end_idx = count - 11

        while len(joltage) < 12:
            digit = max(bank[start_idx:end_idx])
            digit_idx = bank.index(digit, start_idx, end_idx)
            joltage += digit
            start_idx = digit_idx + 1
            end_idx += 1

        total += int(joltage)

    print(total)


part1()
part2()