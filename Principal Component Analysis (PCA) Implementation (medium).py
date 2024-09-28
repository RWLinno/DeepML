import numpy as np 
def pca(data: np.ndarray, k: int) -> list[list[int|float]]:
    principal_components = []
    data = (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    covariance_matrix = np.cov(data, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    principal_components = eigenvectors[:, :k].tolist()

    return principal_components

if __name__=="__main__":
    data = np.array([[1, 2], [3, 4], [5, 6]])
    k = 1
    print(pca(data, k)) # [[-0.70710678], [0], [0.70710678]]