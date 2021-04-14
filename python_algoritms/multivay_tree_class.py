class Tree:
    def __init__(self, kids, next_=None):
        self.kids = self.val = kids
        self.next = next_


t = Tree(Tree("a", Tree("b", Tree("c", Tree("d")))))
print(t.kids.next.next.val)
