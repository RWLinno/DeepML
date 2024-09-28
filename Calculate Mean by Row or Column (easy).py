import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    means = []
    if mode == 'column':
        means = np.mean(matrix, axis=0)
    else:
        means = np.mean(matrix, axis=1)
    return means


if __name__=="__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mode = 'column'
    print(calculate_matrix_mean(matrix, mode))
