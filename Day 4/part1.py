score = 0
with open('input.txt') as f:
    for line in f.readlines():
        a1, a2, b1, b2 = map(int, line.replace(',', '-', 1).split('-'))
        score += (a1 >= b1 and a2 <= b2) or (a1 <= b1 and a2 >= b2)
print(score)