score, state, group = 0, 0, None
with open('input.txt') as f:
    for line in f.readlines():
        cur = set(line[:-1])
        if state == 0:
            group = cur
        elif state == 1:
            group &= cur
        else:
            same = (group & cur).pop()
            dist = ord('A') - 27 if same.isupper() else ord('a') - 1
            score += ord(same) - dist
        state = (state + 1) % 3
print(score)