from functools import cmp_to_key
from itertools import chain, repeat, takewhile

with open('input.txt') as fp:
    d = [eval(x) for x in fp.readlines() if x.strip()] + [s := [[2]], e := [[6]]]
print(((x := sorted(d, key=cmp_to_key(lambda l, r: ((z := (f := lambda a, b: (a, b) if type(a) == type(b) == int else (
    *(a := ([a] if type(a) == int else (a or [-1])), b := ([b] if type(b) == int else (b or [-1])),
      zip(*(x := [[*f(*x)] for x in zip(chain(a, repeat(-1, len(b) - len(a))), chain(b, repeat(-1, len(a) - len(b))))])[
           :len(list(takewhile(lambda y: not (y[0] < y[1] < y[0]), x))) + 1]),)[2],))(l, r))[0] > z[1]) * 2 - 1))
        ).index(s) + 1) * (x.index(e) + 1))
