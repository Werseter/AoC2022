with open('input.txt') as fp:
    data = [x.split() for x in fp.readlines()]
sig = [1]
[sig.append(sig[-1]) if entry == ['noop'] else sig.extend((sig[-1], sig[-1] + int(entry[1]))) for entry in data]
print(sum(sig[x] * (x + 1) for x in [19, 59, 99, 139, 179, 219]))
