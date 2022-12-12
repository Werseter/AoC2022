from collections import defaultdict, deque

with open('input.txt') as fp:
    data = [[ord(y) for y in x.strip()] for x in fp.readlines()]
graph, curr, peak, visited = defaultdict(set), None, None, set()
[[((curr := ((i, j) if x == (s := ord('S')) else curr)), (peak := ((i, j) if x == (e := ord('E')) else peak)),
   [graph[i, j].add((a, b)) if (0 <= a < len(data) and 0 <= b < len(row) and (((y := [(d if (d := data[y][z]) not in (
       s, e) else (ord('z'), ord('a'))[x == s]) for y, z in ((a, b), (i, j))])[0] - y[1]) < 2)) else None for a, b in (
        (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))]) for j, x in enumerate(row)] for i, row in enumerate(data)]
queue = deque([[curr]])
while queue:
    if (node := (path := queue.popleft())[-1]) not in visited:
        if node == peak:
            print(len(path) - 1)
            break
        visited.add(node)
        queue.extend([path + [neighbor] for neighbor in graph[node]])
