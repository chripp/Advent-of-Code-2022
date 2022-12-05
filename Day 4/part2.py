score = 0
with open('input.txt') as f:
    for line in f.readlines():
        a1, a2, b1, b2 = map(int, line.replace(',', '-', 1).split('-'))
        score += a2 >= b1 and b2 >= a1
print(score)