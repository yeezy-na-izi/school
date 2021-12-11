with open('26data/26-s1.txt') as input_file:
    useless = input_file.readline()
    discount = []
    without_discount = []
    for i in input_file:
        price = int(i)
        if price > 150:
            discount.append(price)
        else:
            without_discount.append(price)
    discount.sort()
skidki = discount[:len(discount) // 2]
output = sum(discount[len(discount) // 2:] + without_discount) + sum(skidki) * 0.8
print(output)
print(skidki[-1])