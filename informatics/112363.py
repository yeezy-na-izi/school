class SomeClass:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.sr_mark = sum(marks) / 3

    def __str__(self):
        return f'{self.name} {self.surname}'


x = []
for i in range(int(input())):
    inp = input().split()
    x.append(SomeClass(inp[0], inp[1], [int(i) for i in inp[2:]]))
max1 = x[0]
max2 = 0
max3 = []
for i in x[1:]:
    if max1.sr_mark < i.sr_mark:
        max3 = max2
        max2 = max1
        max1 = i
    elif not max2 or max2.sr_mark < i.sr_mark:
        max3 = max2
        max2 = i
    elif not max3 or max3.sr_mark < i.sr_mark:
        max3 = i
for i in x:
    if max1 == i or max2 == i or max3 == i:
        print(i)
