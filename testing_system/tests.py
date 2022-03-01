import sys
from time import time


def pprint(string):
    sys.stdout.write(string + '\n')


x = time()
for i in range(123000):
    print('something')
    # sys.stdout.write('something' + '\n')
end_print = time() - x
x = time()
q = [1, 2, 3, 4, 5]
for i in range(123000):
    # pprint('something')
    sys.stdout.write('something' + '\n')
end_sys = time() - x
print()
print(f'{end_sys=}')
print(f'{end_print=}')
