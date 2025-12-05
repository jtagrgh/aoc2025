with open('day5.in', 'r') as file:
    lines = file.readlines()

split_idx = lines.index('\n')
ranges = [tuple(map(int, x.strip().split('-'))) for x in lines[:split_idx]]
ids = [int(x.strip()) for x in lines[split_idx+1:]]


def part1():
    print(sum(any(l <= id <= r for l,r in ranges) for id in ids))


def part2():
    ranges.sort()
    merged_ranges = [list(ranges[0])]

    for i,(start, end) in enumerate(ranges[1:], start=1):
        if start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        elif end > merged_ranges[-1][1]:
            merged_ranges[-1][1] = end
    
    print(sum(b-a+1 for a,b in merged_ranges))
        

part1()
part2()