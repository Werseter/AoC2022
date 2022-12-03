with open('input.txt') as fp:
    data = fp.readlines()
print(sum((y := next(iter(set(x[:len(x) // 2]) & set(x[len(x) // 2:]))),
           (ord(y) - (96 if y.islower() else 38)))[1] for x in data))
