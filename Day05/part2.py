with open('input.txt') as fp:
    stack_data, move_data = [x.split('\n') for x in fp.read().rstrip().split('\n\n')]
stacks = {int(k): v for k, *v in ([y for y in reversed(x) if y != ' '] for x in zip(*stack_data) if x[-1] != ' ')}
moves = [[stacks[b].extend([stacks[a].pop() for _ in range(n)][::-1]) for n, a, b in
          [(int(x) for x in move.split() if x.isdigit())]] for move in move_data]
print(''.join(x[-1] for x in stacks.values()))
