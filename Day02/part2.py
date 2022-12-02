with open('input.txt') as fp:
    data = (x.split() for x in fp.readlines())
print(sum((((ord(x) - ord('A') + ord(y) - ord('Y')) % 3 + 1) + (ord(y) - ord('X')) * 3) for x, y in data))
