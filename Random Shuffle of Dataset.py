import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]

if __name__ == '__main__':
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([1, 2, 3, 4])
    print(shuffle_data(X, y))

'''
    output: (array([[5, 6],
                    [1, 2],
                    [7, 8],
                    [3, 4]]), 
             array([3, 1, 4, 2]))
'''