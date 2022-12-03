with open('input.txt') as fp:
    data = [x.strip() for x in fp.readlines()]
print(sum((x := next(iter(set(a) & set(b) & set(c))),
           (ord(x) - (96 if x.islower() else 38)))[1] for a, b, c in zip(data[::3], data[1::3], data[2::3])))
