from cc.from_10_to_p import from_10_to_p
from cc.from_p_to_10 import from_p_to_10
from cc.rod_ss import rod_cc

print('1) Из 10 в P-ичную')
print('2) Из Р-ичной в 10')
print('3) Для родственнных')
z = int(input())
if z == 1:
    number = input('Число через точку ').split('.')
    cc = int(input('Система счисления '))
    from_10_to_p(number, cc)
elif z == 2:
    inp = input('Число через точку ')
    cc = int(input('Система счисления '))
    from_p_to_10(inp, cc)
elif z == 3:
    number = input('Число через точку ').split('.')
    cc = int(input('Система входного '))
    degree = int(input('Степень выходного '))
    print('1) Из меньшей в большую?')
    print('2) Из большей в меньшию?')
    yes_no = input()
    rod_cc(number, cc, degree, yes_no)
