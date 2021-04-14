class Matrix:
    def __init__(self, line=0, column=0, matrix=None):
        if matrix is None:
            matrix = []
        self.line = line
        self.column = column
        self.bin_matrix = matrix

    def m_add(self, number):
        if len(self.bin_matrix) == self.column and len(self.bin_matrix[-1]) == self.line:
            return False
        if not self.bin_matrix or len(self.bin_matrix[-1]) == self.line:
            self.bin_matrix.append([])
        self.bin_matrix[-1].append(number)

    def determinant(self):
        pass

    def det(self):
        return self.determinant()

    def __mul__(self, other):
        if self.column == other.line:
            matrix_to_return = []
            for i in range(self.line):
                matrix_to_return.append([])
                for j in range(other.column):
                    numb = 0
                    for k in range(self.column):
                        numb += self.bin_matrix[i][k] * other.bin_matrix[k][j]
                    matrix_to_return[-1].append(numb)
            return Matrix(len(matrix_to_return), len(matrix_to_return[0]), matrix_to_return)
        return Matrix

    def __add__(self, other):
        if self.column == other.line:
            matrix_to_return = []
            for i in range(self.line):
                matrix_to_return.append([])
                for j in range(other.column):
                    numb = 0
                    for k in range(self.column):
                        numb += self.bin_matrix[i][k] * other.bin_matrix[k][j]
                    matrix_to_return[-1].append(numb)
            return Matrix(len(matrix_to_return), len(matrix_to_return[0]), matrix_to_return)
        return None

    def __len__(self):
        return len(self.bin_matrix)

    def __getitem__(self, item):
        if item > len(self):
            return None
        elif self.line == 1:
            return self.bin_matrix[item]
        else:
            return Matrix(1, self.column, self.bin_matrix[item])

    def __str__(self):
        string = ''
        for i in self.bin_matrix:
            string += ''.join([f'{j:4d}' for j in i]) + '\n'
        return string
    #
    # def __setitem__(self, key, value):
    #     pass


x = [[-16, 9, 11], [9, -3, 0], [31, -3, -11]]
y = [[4], [1], [8]]

first_obj = Matrix(3, 3, x)
second_obj = Matrix(3, 1, y)
x = first_obj * second_obj
print(x)
