with open('input.txt') as fp:
    data = [((x := line.split())[0], int(x[1])) for line in fp.readlines()]
r = [(0, 0) for _ in range(10)]
print(len(set().union(*({([r.insert(0, [*map(sum, zip(r.pop(0), ({a: 1, b: -1}.get(dr, 0) for a, b in ('RL', 'UD'))))]),
                           *[(r.pop(idx) and r.insert(idx, (h[0] - int(x), h[1] - int(y)))) if (-1 < (x := ((h := r[
                               idx - 1])[0] - (t := r[idx])[0]) / 2) < 1) + (-1 < (y := (h[1] - t[1]) / 2) < 1) < 2 else
                             _ for idx in range(1, len(r))]]) and r[-1] for _ in range(dst)} for (dr, dst) in data))))
