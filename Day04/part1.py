with open('input.txt') as fp:
    data = ((range(*(int(a), int(b) + 1)) for a, b in (y.split('-') for y in x.split(','))) for x in fp.readlines())
print(sum((1 for x, y in data if (a := set(x)) <= (b := set(y)) or b <= a)))
