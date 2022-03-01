with open('26data/26-42.txt') as file_input:
    useless, money = [int(i) for i in file_input.readline().split()]
    a_type = []
    b_type = []
    for string in file_input:
        letter, price, count = string.split()
        if letter == 'Z':
            # a_type.append((int(price), int(count)))
            money -= int(price) * int(count)
        else:
            b_type.append((int(price), int(count)))
    print(money)
    counter = 0
    for i in sorted(b_type, key=lambda el: el[0]):
        if money >= i[0] * i[1]:
            counter += i[1]
            money -= i[0] * i[1]
        else:
            counter += money // i[0]
            money -= i[0] * (money // i[0])
            print(f'{money = }')
            print(f'{counter = }')
            break

