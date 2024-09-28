def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n, m = len(vectors), len(vectors[0]) #features and observations
    covariance_matrix = [[0 for i in range(n)] for j in range(n)]
    means = [sum(feature) / m for feature in vectors]
    for i in range(n):
        for j in range(i, n):
            cov = sum((vectors[i][k] - means[i]) * (vectors[j][k] - means[j]) for k in range(m)) / (m - 1)
            covariance_matrix[i][j] = covariance_matrix[j][i]= cov
            
    return covariance_matrix

if __name__=="__main__":
    vectors = [[1, 2, 3], [4, 5, 6]]
    print(calculate_covariance_matrix(vectors)) # [[1.0, 1.0], [1.0, 1.0]]