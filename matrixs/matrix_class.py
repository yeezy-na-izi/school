import copy


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
        d = 1
        columns = 0
        copy_matrix = copy.deepcopy(self)
        for i in range(copy_matrix.line - 1):
            z = copy_matrix.bin_matrix[i][columns]
            ma = i
            for j in range(i + 1, copy_matrix.line):
                if abs(copy_matrix.bin_matrix[j][columns]) > abs(z):
                    z = copy_matrix[j][columns]
                    ma = i
            if z == 0:
                return 0
            elif ma == i:
                d *= z
            else:
                d *= -z
                copy_matrix.bin_matrix[i], copy_matrix.bin_matrix[ma] = copy_matrix.bin_matrix[ma], \
                                                                        copy_matrix.bin_matrix[i]
            constriction_x = copy_matrix.get_constriction()
            for j in range(constriction_x.line):
                for g in range(constriction_x.column):
                    constriction_x.bin_matrix[j][g] -= copy_matrix[j + 1][0] * copy_matrix[0][g + 1] / copy_matrix[i][0]

        print(d)

    def det(self):
        return self.determinant()

    def get_constriction(self):
        constriction_m = copy.deepcopy(self)
        for i in range(constriction_m.column):
            constriction_m.bin_matrix[i] = constriction_m.bin_matrix[i][1:]

        constriction_m.bin_matrix = constriction_m.bin_matrix[1:]
        constriction_m.line -= 1
        constriction_m.column -= 1

        return constriction_m

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
    def __setitem__(self, key, value):
        if key > len(self):
            return None
        self.bin_matrix[key] = value
        return self


x = [[3, 2, 1], [5, 3, 6], [4, 3, 6]]
y = [[4], [1], [8]]

first_obj = Matrix(3, 3, x)
second_obj = Matrix(3, 1, y)
print(first_obj.determinant())
