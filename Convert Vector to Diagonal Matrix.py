import numpy as np

def make_diagonal(x):
    return np.diag(x)

if __name__ == '__main__':
    x = np.array([1, 2, 3])
    output = make_diagonal(x)
    print(output)