score = 0
base = ord('A')
dist = ord('X') - ord('A')
with open('input.txt') as f:
    for line in f.readlines():
        a, b = ord(line[0])-base, ord(line[2])-dist-base
        if a == b:
            result = 3
        elif (a + 1) % 3 == b:
            result = 6
        else:
            result = 0
        score += result + b + 1

print(score)