cur_val, max_vals = 0, []
min_id = None
with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            if min_id is None:
                max_vals.append(cur_val)
                if len(max_vals) == 3:
                    min_id = max_vals.index(min(max_vals))
            elif cur_val > max_vals[min_id]:
                max_vals[min_id] = cur_val
                min_id = max_vals.index(min(max_vals))
            cur_val = 0
        else:
            cur_val += int(line)
max_vals[min_id] = max(max_vals[min_id], cur_val)
print(sum(max_vals))