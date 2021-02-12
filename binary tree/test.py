class Node:
    def __init__(self, value, left=None, right=None):
        self.key = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'{self.key}'


class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while True:
            if value < curr.key:
                if curr.left is None:
                    curr.left = node
                    break
                else:
                    curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    break
                else:
                    curr = curr.right


x = Node(10)
print(x)
