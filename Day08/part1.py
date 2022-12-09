with open('input.txt') as fp:
    data = [[int(x) for x in line.strip()] for line in fp.readlines()]
print(sum(map(sum, ([1 for i, (x, col) in enumerate(zip(row, zip(*data))) if
                     any(x > y for y in (max(it or [-1]) for it in (
                         row[:i], row[i + 1:], col[:j], col[j + 1:])))] for j, row in enumerate(data)))))
