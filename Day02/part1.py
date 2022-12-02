with open('input.txt') as fp:
    data = (x.split() for x in fp.readlines())
print(sum((ord(y) - ord('W') + (((ord(y) - ord('X') - ord(x) + ord('A') + 1) % 3) * 3)) for x, y in data))
