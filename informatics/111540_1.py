count_point, amount = [int(i) for i in input().split()]
output = []
almost_output = []

for i in range(amount):
    string = [int(i) for i in input().split()]
    for j in string:
        if j in almost_output:
