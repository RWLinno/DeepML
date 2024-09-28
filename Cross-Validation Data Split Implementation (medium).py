import numpy as np

def cross_validation_split(data, k):
#    np.random.shuffle(data)
    fold_size = len(data) // k
    folds = []

    for i in range(k):
        start, end = i * fold_size, (i + 1) * fold_size if i != k-1 else len(data)
        test = data[start: end]
        train = np.concatenate([data[:start], data[end:]])
        folds.append((train.tolist(), test.tolist()))
    return folds

if __name__ == '__main__':
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    k = 5
    print(cross_validation_split(data, k))