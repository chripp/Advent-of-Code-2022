score = 0
base = ord('A')
dist = ord('X') - ord('A')
with open('input.txt') as f:
    for line in f.readlines():
        a, b = ord(line[0])-base, line[2]
        if b == 'X': #Lose
            b_n = (a - 1) % 3
            result = 0
        elif b == 'Y': #Draw
            b_n = a
            result = 3
        else: #Win
            b_n = (a + 1) % 3
            result = 6

        score += result + b_n + 1

print(score)