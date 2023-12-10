import random
import numpy as np

class Matrix:

    def __init__(self, data):
        self.data = np.array(data, dtype=int)

    def __add__(self, other):
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        return Matrix(self.data @ other.data)

    def write_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

    def __str__(self):
        s = ""
        for row in result_add.data:
            s += ' '.join(map(str, row)) + '\n'
        return s

    @property
    def shape(self):
        return self.data.shape

    @property
    def rows(self):
        return self.data.shape[0]

    @property
    def cols(self):
        return self.data.shape[1]


random.seed(110)
matrix1 = Matrix([[random.randint(0, 10) for _ in range(10)] for _ in range(10)])
matrix2 = Matrix([[random.randint(0, 10) for _ in range(10)] for _ in range(10)])

result_add = matrix1 + matrix2
result_mul = matrix1 * matrix2
result_matmul = matrix1 @ matrix2

matrix1.write_to_file('artifacts/matrix1.txt')
matrix2.write_to_file('artifacts/matrix2.txt')

result_add.write_to_file('artifacts/matrix+.txt')
result_mul.write_to_file('artifacts/matrix*.txt')
result_matmul.write_to_file('artifacts/matrix@.txt')
