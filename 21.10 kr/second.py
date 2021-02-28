def height(self):
    if self.value is None:
        return 0
    lheight = self.left.height()
    rheight = self.right.height()
    if lheight > rheight:
        return lheight + 1
    return rheight + 1