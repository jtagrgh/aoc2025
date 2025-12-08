from itertools import combinations
from math import sqrt, prod


with open('day8.in', 'r') as file:
    lines = [x.strip() for x in file.readlines()]

nodes = [tuple(map(int, line.split(','))) for line in lines]

dist = lambda a,b: sqrt(sum((x-y)**2 for x,y in zip(a,b)))


def part1():
    node_combinations = sorted([(dist(a,b), a, b) for a,b in combinations(nodes, 2)], reverse=True)

    graph = {node:[] for node in nodes}

    for _ in range(1000):
        _,a,b = node_combinations.pop()
        graph[a].append(b)
        graph[b].append(a)

    visited = set()

    def ffill(node):
        if node in visited:
            return 0
        
        node_count = 0
        stack = [node]
        while stack:
            vis_node = stack.pop()
            if vis_node in visited:
                continue
            visited.add(vis_node)
            node_count += 1
            stack.extend(graph[vis_node])

        return node_count

    node_counts = []

    for node in graph.keys():
        node_counts.append(ffill(node))

    node_counts.sort()

    print(prod(node_counts[-3:]))


def part2():
    node_combinations = sorted([(dist(a,b), a, b) for a,b in combinations(nodes, 2)], reverse=True)

    graph = {node:[] for node in nodes}

    def gt_one_subgraph():
        visited = set()

        subgraph_count = 0

        for node in graph.keys():
            node_count = 0
            stack = [node]

            while stack:
                vis_node = stack.pop()
                if vis_node in visited:
                    continue
                visited.add(vis_node)
                node_count += 1
                stack.extend(graph[vis_node])

            if node_count > 0:
                subgraph_count += 1

            if subgraph_count > 1:
                return True
        
        return False
    
    a = b = (0,0,0)

    while gt_one_subgraph():
        _,a,b = node_combinations.pop()
        graph[a].append(b)
        graph[b].append(a)

    print(a[0] * b[0])


def part2_union():
    node_combinations = sorted([(a, b) for a,b in combinations(nodes, 2)], key=lambda x: dist(*x), reverse=True)
    node_idx = {node:i for i,node in enumerate(nodes)}
    parent = [i for i in range(len(node_idx))]
    size = [1 for _ in parent]

    def find(node):
        if parent[node] == node:
            return node
        parent[node] = find(parent[node])
        return parent[node]
    
    def union(x, y):
        x,y = find(x), find(y)
        if x == y:
            return False
        x,y = sorted([x,y], key=lambda a: size[a])
        parent[x] = y
        size[y] += size[x]
        return True
    
    subgraph_count = len(nodes)

    a = b = (0,0,0)

    while subgraph_count > 1:
        a,b = node_combinations.pop()
        if union(node_idx[a],node_idx[b]):
            subgraph_count -= 1

    print(a[0] * b[0])


def part2_sets():
    circuits = {frozenset([node]) for node in nodes}
    node_combinations = sorted([(a, b) for a,b in combinations(nodes, 2)], key=lambda x: dist(*x), reverse=True)

    a = b = (0,0,0)

    while len(circuits) > 1:
        a,b = node_combinations.pop()
        circ_a = next(circ for circ in circuits if a in circ)
        circ_b = next(circ for circ in circuits if b in circ)

        circuits.discard(circ_a)
        circuits.discard(circ_b)

        circuits.add(circ_a | circ_b)

    print(a[0] * b[0])


part1()
part2()
part2_union()
part2_sets()