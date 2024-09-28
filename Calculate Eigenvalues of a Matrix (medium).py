import numpy as np

def calculate_eigenvalues(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues

if __name__=="__main__":
    matrix = [[2, 1], [1, 2]]
    print(calculate_eigenvalues(matrix)) # output: [3., 1.]