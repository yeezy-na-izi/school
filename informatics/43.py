from sys import stdin

products = {}
sold_for_amount = 0


def add_product(name, count=0, price=0):
    if name in products:
        products[name][0] += count
        return f'Количество товара обновлено теперь {products[name][0]}'
    else:
        products[name] = [count, price]
        return 'Товар успешно добавлен на склад'


def sell_product(name, count=0):
    global sold_for_amount
    if products[name] >= count:
        sold_for_amount += count * products[name][1]
        products[name][0] -= count
        return f'Осталось {products[name][0]} {name}'
    else:
        output = products[name][0]
        sold_for_amount += output * products[name][1]
        products[name][0] = 0
        return f'Я смог продать только {output} {name}'


def finish():
    money = 0
    for i in products:
        money += products[i][0] * products[i][1]
    return money


print('Всем привет это склад Кати Захаровой и тут такие правила:')
print('1) Если хотите добавить товар вводите в формате "добавить {название} {количество} {цела}"')
print('2) Если хотите продать товар вводите в формате "продать {название} {количество}"')
print('3) Если хотите узнать насколько успешно вы все продали и на какую сумму осталось товара на складе смело'
      ' пишите "закончить" или нажимайте ctrl + d')
print('Будьте лапочками')

for string in stdin:
    info = string.split()
    if info[0].lower() == 'добавить':
        print(add_product(info[1], int(info[2]), int(info[3])))
    elif info[0].lower() == 'продать':
        print(sell_product(info[1], int(info[2])))
    elif info[0].lower() == 'закончить':
        break

print(f'Вы продали на сумму {sold_for_amount}\n'
      f'На складе товаров еще на сумму {finish()}')
