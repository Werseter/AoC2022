with open('input.txt') as fp:
    data = fp.read().strip()
print(next(n + len(z) for n, *y in enumerate(zip(*(data[x:] for x in range(4)))) if len(z := list(*y)) == len(set(z))))
