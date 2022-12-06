length = 14
with open('input.txt') as f:
    line = f.readline()
    i = 0
    while i+length <= len(line):
        found = set()
        for j in range(1, length+1):
            pos = i+length-j
            if line[pos] in found:
                i = pos+1
                break
            found.add(line[pos])
        else:
            print(i+length)
            break