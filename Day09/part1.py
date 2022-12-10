with open('input.txt') as fp:
    data = [((x := line.split())[0], int(x[1])) for line in fp.readlines()]
r = [(0, 0) for _ in range(2)]
print(len(set().union(*({(r := [h := [*map(sum, zip(r[0], ({a: 1, b: -1}.get(dr, 0) for a, b in ('RL', 'UD'))))],
        (h[0] - int(x), h[1] - int(y)) if (-1 < (x := (h[0] - (t := r[-1])[0]) / 2) < 1) !=
           (-1 < (y := (h[1] - t[1]) / 2) < 1) else t])[-1] for _ in range(dst)} for (dr, dst) in data))))
