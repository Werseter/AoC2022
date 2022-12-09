from functools import reduce
from itertools import takewhile
from operator import mul

with open('input.txt') as fp:
    data = [[int(x) for x in line.strip()] for line in fp.readlines()]
print(max(map(max, ([reduce(mul, [len((z := list(takewhile(lambda z: z < x, y))) + list(y)[len(z):len(z) + 1]) for y in
                                  (row[:i][::-1], row[i + 1:], col[:j][::-1], col[j + 1:])]) for i, (x, col) in
                     enumerate(zip(row, zip(*data)))] for j, row in enumerate(data)))))
