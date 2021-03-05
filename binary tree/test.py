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

    def display(self, level=0):
        lines, *_ = self.display_helper()
        for line in lines:
            print(line)
        # if self.value is not None:
        #     self.left.display(level + 1)
        #     print(' ' * 4 * level + '->', self.value)
        #     self.right.display(level + 1)

    def display_helper(self):
        if self.right is None and self.left is None:
            line = str(self.value)
            width = len(line)
            return [line], width, 1, width // 2

        if self.right is None:
            lines, height, width, x_pos = self.left.display_helper()
            str_value = str(self.value)
            len_value = len(str_value)
            line_left_number = (x_pos + 1) * ' ' + (height - x_pos - 1) * '_' + str_value
            line_without_number = x_pos * ' ' + '/' + (height - x_pos - 1 + len_value) * ' '
            line_right_number = [line + len_value * ' ' for line in lines]
            return [line_left_number,
                    line_without_number] + line_right_number, height + len_value, width + 2, height + len_value // 2

        if self.left is None:
            lines, height, width, x_pos = self.right.display_helper()
            str_value = str(self.value)
            len_value = len(str_value)
            line_left_number = str_value + x_pos * '_' + (height - x_pos) * ' '
            line_without_number = (len_value + x_pos) * ' ' + '\\' + (height - x_pos - 1) * ' '
            line_right_number = [len_value * ' ' + line for line in lines]
            return [line_left_number,
                    line_without_number] + line_right_number, height + len_value, width + 2, len_value // 2

        left, height_left, width_left, x_pos = self.left.display_helper()
        right, height_right, width_right, y_pos = self.right.display_helper()
        str_value = str(self.value)
        len_value = len(str_value)
        line_left_number = f'{(x_pos + 1) * " "}{(height_left - x_pos - 1) * "_"}{str_value}{y_pos * "_"}{(height_right - y_pos) * " "}'
        line_without_number = f'{x_pos * " "}/{(height_left - x_pos - 1 + len_value + y_pos) * " "}\\{(height_right - y_pos - 1) * " "}'
        if width_left < width_right:
            left += [height_left * ' '] * (width_right - width_left)
        elif width_right < width_left:
            right += [height_right * ' '] * (width_left - width_right)
        return [line_left_number, line_without_number] + [a + len_value * ' ' + x for a, x in zip(left, right)], \
               height_left + height_right + len_value, \
               max(width_left, width_right) + 2, \
               height_left + len_value // 2

    def height(self, node):
        if node is None:
            return 0
        l_height = self.height(node.left)
        r_height = self.height(node.right)
        if l_height > r_height:
            return l_height + 1
        return r_height + 1


b = BalancedTree(50)
# a = BalancedTree(50)
for i in range(60):
    x = random.randint(0, 200)
    b.insert(x)
    # a.insert_without_balance(x)
b.display()
# a.display()
# q = input()
# for i in q:
#     b.insert(int(i))
#     a.insert_without_balance(int(i))
# b.display()
# a.display()
