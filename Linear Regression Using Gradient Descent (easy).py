import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    for _ in range(iterations):
        error = X @ theta - y.reshape(-1,1) # 3*2 @ 2*1 - 3*1 = 3*1
        update = X.T @ error / m
        theta = theta - alpha * update # 2*1 - 0.01*(2*3)*(3*1)
        
    return np.round(theta.flatten(), 4)

if __name__ == "__main__":
    X = np.array([[1, 1], [1, 2], [1, 3]]) # 3*2 -> 2*1
    y = np.array([1, 2, 3]) # 3*1
    alpha = 0.01
    iterations = 1000
    print(linear_regression_gradient_descent(X, y, alpha, iterations)) # [[-0.5], [1.0]]