import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    L = len(A)
    nda= A - np.diag(np.diag(A))
    x = [0 for i in range(L)]
    x_update = [0 for i in range(L)]  
    for iter in range(n):
        for i in range(L):
            x_update[i] = (b[i] - sum(nda[i]*x)) / A[i][i]
        x = x_update.copy()
    return x

if __name__=="__main__":
    A = [[5, -2, 3], [-3, 9, 1], [2, -1, -7]]
    b = [-1, 2, 3]
    n=2
    print(solve_jacobi(A, b, n)) # output: [0.146, 0.2032, -0.5175]