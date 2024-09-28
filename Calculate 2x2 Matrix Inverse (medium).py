import numpy as np

def inverse_2x2(matrix):
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    det = a * d - b * c
    inverse = [[d, -b], [-c, a]]
    inverse =  np.mat(inverse) / det
    return inverse

if __name__ == '__main__':
    matrix = [[4, 7], [2, 6]]
    print(inverse_2x2(matrix)) # [[0.6, -0.7], [-0.2, 0.4]]