import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    b = np.mat(a).T
    return b

if __name__=="__main__":
    a = [[1,2,3],[4,5,6]]
    print(transpose_matrix(a))
