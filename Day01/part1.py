with open('input.txt') as fp:
    data = ([int(y) for y in x.split('\n')] for x in fp.read().strip().split('\n\n'))
print(max(sum(x) for x in data))
