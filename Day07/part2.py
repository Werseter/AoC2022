from collections import defaultdict
from functools import reduce

with open('input.txt') as fp:
    data = fp.readlines()
fs, cwd = (fs_init := lambda: defaultdict(fs_init))(), []
[(((cwd.clear(), cwd.append('/')) if x[2] == '/' else cwd.pop() if x[2] == '..' else
   cwd.append(f'{cwd[-1]}{x[2]}/')) if (x := cmd.split())[0:2] == ['$', 'cd'] else (None if not x[0].isdigit() else
  (reduce(lambda x, y: x[y], cwd, fs).update({f'{cwd[-1]}{x[1]}': int(x[0])})))) for cmd in data]
dir_sizes = (collapse := lambda v: reduce(lambda x, y: [x[0] + v.pop(y[0]), x[1]] if type(y[1]) == int else (
    [x[0] + (z := collapse(v.pop(y[0])))[0], {**x[1], **{y[0]: z[0]}, **z[1]}]), v.copy().items(), [0, v]))(fs)[1]
print(next(x for x in sorted(dir_sizes.values()) if x >= dir_sizes['/'] - 40000000))
