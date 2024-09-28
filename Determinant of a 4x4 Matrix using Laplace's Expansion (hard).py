
def determinant_3x3(matrix):
    """
    计算 3x3 矩阵的行列式
    :param matrix: 3x3 矩阵，形式为 [[a, b, c], [d, e, f], [g, h, i]]
    :return: 行列式的值
    """
    a, b, c, d, e, f, g, h, i = matrix
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

def construct3x3(matrix: list[list[int|float]], col: int) -> float:
    res = []
    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if j != col and j != col:
                res.append(matrix[i][j])
    return determinant_3x3(res)

def determinant_4x4(matrix: list[list[int|float]]) -> float:
    res = 0
    for i in range(len(matrix)):
        res += matrix[0][i] * construct3x3(matrix, i) * (-1)**i
    return res

if __name__=="__main__":
    a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(determinant_4x4(a)) # output: 0.0