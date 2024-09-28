def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    result = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] * scalar
    return result

if __name__=="__main__":
    matrix = [[1, 2], [3, 4]]
    scalar = 2
    print(scalar_multiply(matrix, scalar)) # [[2, 4], [6, 8]]