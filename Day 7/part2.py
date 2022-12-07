class Dir():
    def __init__(self, parent):
        self.parent = parent
        self.done = False
        self.file_size = 0
        self.next = {}
        self.size = None

    def calc_size(self):
        self.size = self.file_size + sum(map(Dir.calc_size, self.next.values()))
        return self.size

    def get_res(self, needed):
        best = self.size
        if best < needed:
            return None
        for next in self.next.values():
            sub = next.get_res(needed)
            if sub is not None and sub < best:
                best = sub
        return best

tree = Dir(None)
cur = tree
in_ls = False
with open('input.txt') as f:
    for line in f.readlines():
        splits = line[:-1].split()
        if splits[0] == '$':
            if in_ls:
                cur.done = True
                in_ls = False
            if splits[1] == 'cd':
                if splits[2] == '/':
                    cur = tree
                elif splits[2] == '..':
                    cur = cur.parent
                else:
                    cur = cur.next[splits[2]]
            else:
                in_ls = True
        else:
            if not cur.done:
                if splits[0] == 'dir':
                    cur.next[splits[1]] = Dir(cur)
                else:
                    cur.file_size += int(splits[0])
tree.calc_size()
print(tree.get_res(30000000 - (70000000 - tree.size)))
