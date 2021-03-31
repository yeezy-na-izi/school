a = []
b = []


def prod_matrix(x, y):
    if len(x[0]) == len(y):
        matrix_to_return = []
        for i in range(len(x)):
            matrix_to_return.append([])
            for j in range(len(y[0])):
                numb = 0
                for k in range(len(x[0])):
                    numb += x[i][k] * y[k][j]
                matrix_to_return[-1].append(numb)
        return matrix_to_return
    return False


def sum_matrix(x, y):
    matrix_to_return = []
    if len(x) == len(y) and len(x[0]) == len(y[0]):
        for i in range(len(x)):
            matrix_to_return.append([])
            for j in range(len(x[0])):
                matrix_to_return[-1].append(x[i][j] + y[i][j])
        return matrix_to_return
    return False


def numb_matrix(numb, x):
    matrix_to_return = []
    for i in range(len(x)):
        matrix_to_return.append([])
        for j in range(len(x[0])):
            matrix_to_return[-1].append(numb * x[i][j])
    return matrix_to_return


stroka = [int(i) for i in input().split()]
while stroka:
    a.append(stroka)
    stroka = [int(i) for i in input().split()]

stroka = [int(i) for i in input().split()]
while stroka:
    b.append(stroka)
    stroka = [int(i) for i in input().split()]
w = sum_matrix(a, b)
print(prod_matrix(w, w) == sum_matrix(sum_matrix(prod_matrix(a, a), prod_matrix(b, b)), numb_matrix(2, prod_matrix(a, b))))
