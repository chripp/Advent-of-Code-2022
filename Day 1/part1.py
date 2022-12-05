cur_val, max_val = 0, 0
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            max_val = max(max_val, cur_val)
            cur_val = 0
        else:
            cur_val += int(line)
max_val = max(max_val, cur_val)
print(max_val)