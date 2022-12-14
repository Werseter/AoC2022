from itertools import chain, repeat, takewhile

with open('input.txt') as fp:
    d = [[eval(y) for y in x.split()] for x in fp.read().split('\n\n')]
print(sum(i for i, (x, y) in enumerate(d, 1) if (z := (align := lambda a, b: (a, b) if type(a) == type(b) == int else (
    *(a := ([a] if type(a) == int else (a or [-1])), b := ([b] if type(b) == int else (b or [-1])), zip(*(x := [
        [*align(*x)] for x in zip(chain(a, repeat(-1, len(b) - len(a))), chain(b, repeat(-1, len(a) - len(b))))])[:len(
            list(takewhile(lambda y: not (y[0] < y[1] < y[0]), x))) + 1]),)[2],))(x, y))[0] < z[1]))
