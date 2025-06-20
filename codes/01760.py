class Trie:
    def __init__(self):
        self.root = dict()
    def add_path(self, s):
        root = self.root
        for path in s:
            if path not in root:
                root[path] = dict()
            root = root[path]
        root['end'] = True
        return self.root

def parse_tree(prev, root):
    """
    用这种方式实现换行打印还是很方便的！
    """
    for key in sorted(root.keys()):
        if key != 'end':
            print(f'{prev}{key}')
            parse_tree(prev+' ', root[key])

trie = Trie()
n = int(input())
for _ in range(n):
    s = list(input().split('\\'))
    root = trie.add_path(s)
parse_tree('', root)