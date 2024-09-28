import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
    subsets = []
    n_samples = np.shape(X)[0]
    np.random.seed(seed)
    X_y = np.concatenate((X, y.reshape((len(y), 1))), axis=1)
    np.random.shuffle(X_y)
    subsample_size = n_samples if replacements else n_samples // 2
    for _ in range(n_subsets):
        idx = np.random.choice(range(n_samples), size=subsample_size, replace=replacements)
        X_subset = X_y[idx][:, :-1]
        y_subset = X_y[idx][:, -1]
        subsets.append([X_subset, y_subset])
    return subsets

if __name__ == '__main__':
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    y = np.array([1, 2, 3, 4, 5])
    n_subsets = 3
    replacements = False
    print(get_random_subsets(X, y, n_subsets))

'''
    Output:
    [array([[7, 8],
            [1, 2]]), 
     array([4, 1])]
     
    [array([[9, 10],
            [5, 6]]), 
     array([5, 3])]
     
    [array([[3, 4],
            [5, 6]]), 
     array([2, 3])]
'''