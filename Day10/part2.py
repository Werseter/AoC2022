with open('input.txt') as fp:
    data = [x.split() for x in fp.readlines()]
sig = [1]
[sig.append(sig[-1]) if entry == ['noop'] else sig.extend((sig[-1], sig[-1] + int(entry[1]))) for entry in data]
[print('#' if abs(x - (idx % 40)) < 2 else '.', end='' if idx % 40 != 39 else '\n') for idx, x in enumerate(sig)]
