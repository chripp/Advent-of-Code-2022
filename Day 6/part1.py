with open('input.txt') as f:
    line = f.readline()
    for i in range(len(line) - 4):
        if len(set(line[i:i+4])) == 4:
            print(i+4)
            break