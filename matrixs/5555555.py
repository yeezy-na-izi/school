class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
            else:
                return
        else:
            self.value = value

    def __str__(self):
        if self.value is None:
            return ''
        return '\n'.join(
            f'{self.left if self.left else ""}   '
            f'{self.value if self.value else ""} '
            f'{self.right if self.right else ""} '.split())

    def height(self, node):
        if node is None:
            return 0
        lheight = self.height(node.left)
        rheight = self.height(node.right)
        if lheight > rheight:
            return lheight + 1
        return rheight + 1

    def min(self):
        if self.left is None:
            print(self.value)
        else:
            self.left.min()

    def max(self):
        if self.right is None:
            print(self.value)
        else:
            self.right.max()

    def __contains__(self, item):
        if str(item) in str(self).split():
            return 'YES'
        return 'NO'

    def __len__(self):
        x = len(str(self))
        return x // 2 + 1


inp = [int(i) for i in input().split()]
Tree = Node(inp[0])
for i in inp[1:-1]:
    Tree.insert(i)
print(Tree)
