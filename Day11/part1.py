from functools import partial

with open('input.txt') as fp:
    data = [[y.split(':')[1].strip() for y in x.split('\n')[1:]] for x in fp.read().strip().split('\n\n')]
monkeys = [[[int(x) for x in rules[0].split(',')], partial(lambda dst, md, x: monkeys[dst[x % md == 0]][0].append(x),
            [int(rules[x].split()[-1]) for x in (4, 3)], int(rules[2].split()[-1])), {0: 0},
            partial(lambda evl, old: eval(evl) // 3, rules[1].split('=')[1])] for rules in data]
[[[t(o(i)) for i in l] and c.update({0: c[0] + len(l)}) or l.clear() for l, t, c, o in monkeys] for _ in range(20)]
print((counts := sorted([x[2][0] for x in monkeys], reverse=True))[0] * counts[1])
