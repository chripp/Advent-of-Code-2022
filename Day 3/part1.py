score = 0
with open('input.txt') as f:
    for line in f.readlines():
        middle = (len(line)-1)//2
        same = (set(line[:middle]) & set(line[middle:-1])).pop()
        dist = ord('A') - 27 if same.isupper() else ord('a') - 1
        score += ord(same) - dist
print(score)