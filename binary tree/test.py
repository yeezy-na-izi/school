import random
import copy


class BalancedTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.f = 0

    def insert_without_balance(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BalancedTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BalancedTree(value)
                else:
                    self.right.insert(value)
            else:
                return
        else:
            self.value = value

    def insert(self, value):
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BalancedTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BalancedTree(value)
                else:
                    self.right.insert(value)
            else:
                return
            self.f = self.height(self.left) - self.height(self.right)
            self.balance()
        else:
            self.value = value

    def __str__(self):
        if self.value is None:
            return ''
        return ' '.join(f'{self.left if self.left else ""} '
                        f'{self.value if self.value else ""} '
                        f'{self.right if self.right else ""}'
                        .split())

    def balance(self):
        if self.f == 2:
            if self.left.f < 0:
                self.left.small_left()
            self.small_right()
        if self.f == -2:
            if self.right.f > 0:
                self.right.small_right()
            self.small_left()

    def small_left(self):
        right = self.right
        self.right = right.left
        right.left = copy.deepcopy(self)
        self.right = right.right
        self.value = right.value
        self.left = right.left

    def small_right(self):
        left = self.left
        self.left = left.right
        left.right = copy.deepcopy(self)
        self.right = left.right
        self.value = left.value
        self.left = left.left

    def display(self):
        lines, *_ = self.display_helper()
        for line in lines:
            print(line)

    def display_helper(self):
        if self.right is None and self.left is None:
            line = str(self.value)
            width = len(line)
            return [line], width, 1, width // 2

        if self.right is None:
            lines, n, p, x = self.left.display_helper()
            s = str(self.value)
            u = len(s)
            line_with_number = (x + 1) * ' ' + (n - x - 1) * '_' + s
            line_without_number = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [line_with_number, line_without_number] + shifted_lines, n + u, p + 2, n + u // 2

        if self.left is None:
            lines, n, p, x = self.right.display_helper()
            s = str(self.value)
            u = len(s)
            line_with_number = s + x * '_' + (n - x) * ' '
            line_without_number = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [line_with_number, line_without_number] + shifted_lines, n + u, p + 2, u // 2

        left, n, p, x = self.left.display_helper()
        right, m, q, y = self.right.display_helper()
        s = str(self.value)
        u = len(s)
        line_with_number = f'{(x + 1) * " "}{(n - x - 1) * "_"}{s}{y * "_"}{(m - y) * " "}'
        line_without_number = f'{x * " "}/{(n - x - 1 + u + y) * " "}\\{(m - y - 1) * " "}'
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        return [line_with_number, line_without_number] + [a + u * ' ' + x for a, x in zip(left, right)], \
               n + m + u, max(p, q) + 2, n + u // 2

    def height(self, node):
        if node is None:
            return 0
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        if l_height > r_height:
            return l_height + 1
        return r_height + 1


b = BalancedTree(50)
a = BalancedTree(50)
for i in range(60):
    x = random.randint(0, 200)
    b.insert(x)
    a.insert_without_balance(x)
b.display()
# a.display()
# q = input()
# # for i in q:
# #     b.insert(int(i))
# #     a.insert_without_balance(int(i))
# # b.display()
# # a.display()
