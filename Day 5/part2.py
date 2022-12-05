from collections import deque
stacks = None
in_setup = True
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            continue
        if in_setup:
            if not '[' in line:
                in_setup = False
                continue
            if stacks is None:
                stacks = [deque() for _ in range(len(line)//4)]
            for i, c in enumerate(line[1::4]):
                if c != ' ':
                    stacks[i].appendleft(c)
        else:
            num, origin, dest = map(int, line.split()[1::2])
            stacks[dest-1].extend(reversed([stacks[origin-1].pop() for _ in range(num)]))
print(''.join(stack.pop() for stack in stacks))