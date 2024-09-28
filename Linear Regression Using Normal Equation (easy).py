import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # X(3*2) @ theta(2*1) = y(3*1)
    # XT(2*3) @ X(3*2) @ theta(2*1) = XT(2*3) @ y(3*1)
    # theta = (XT @ X)^-1 @ XT @ y
    X = np.mat(X)
    theta = (X.T @ X).I @ X.T @ np.array(y)
    return np.round(theta, 4).flatten().tolist()

if __name__ == "__main__":
    X = [[1, 1], [1, 2], [1, 3]]
    y = [1, 2, 3]
    print(linear_regression_normal_equation(X, y)) #  [0.0, 1.0]