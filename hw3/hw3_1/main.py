import random


class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")

        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)



    def __mul__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions")

        result_data = [[self.data[i][j] * other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result_data)

    def __matmul__(self, other):
        if self.cols != other.rows:
            raise ValueError("Invalid dimensions")

        result_data = [
            [sum(self.data[i][k] * other.data[k][j] for k in range(self.cols)) for j in range(other.cols)] for i in
            range(self.rows)]
        return Matrix(result_data)



random.seed(0)
matrix1 = Matrix([[random.randint(0, 10) for _ in range(10)] for _ in range(10)])
matrix2 = Matrix([[random.randint(0, 10) for _ in range(10)] for _ in range(10)])

result_add = matrix1 + matrix2
result_mul = matrix1 * matrix2
result_matmul = matrix1 @ matrix2



with open('artifacts/matrix+.txt', 'w') as f:
    for row in matrix1.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in matrix2.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in result_add.data:
        f.write(' '.join(map(str, row)) + '\n')

with open('artifacts/matrix*.txt', 'w') as f:
    for row in matrix1.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in matrix2.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in result_mul.data:
        f.write(' '.join(map(str, row)) + '\n')

with open('artifacts/matrix@.txt', 'w') as f:
    for row in matrix1.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in matrix2.data:
        f.write(' '.join(map(str, row)) + '\n')
    f.write('\n')
    for row in result_matmul.data:
        f.write(' '.join(map(str, row)) + '\n')