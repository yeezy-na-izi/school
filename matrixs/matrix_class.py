class Matrix:
    def __init__(self, x, y, matrix=None):
        if matrix is None:
            matrix = []
        self.line = x
        self.column = y
        self.matrix = matrix

    def create(self, number):
        if len(self.matrix) == self.column and len(self.matrix[-1]) == self.line:
            return False
        if not self.matrix or len(self.matrix[-1]) == self.line:
            self.matrix.append([])
        self.matrix[-1].append(number)

    def __mul__(self, other):
        if len(self.matrix[0]) == len(other.matrix):
            matrix_to_return = []
            for i in range(len(self.matrix)):
                matrix_to_return.append([])
                for j in range(len(other.matrix[0])):
                    numb = 0
                    for k in range(len(self.matrix[0])):
                        numb += self.matrix[i][k] * other.matrix[k][j]
                    matrix_to_return[-1].append(numb)
            self.matrix = matrix_to_return
            print('Done')
        print('Не получилось')


x = Matrix()
y = Matrix()
print(x * y)
