
import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = (data - np.mean(data, axis=0))/np.std(data, axis=0)
    normalized_data = (data - np.min(data, axis=0))/(np.max(data, axis=0) - np.min(data, axis=0))
    return standardized_data, normalized_data

if __name__=="__main__":
    data = np.array([[1, 2], [3, 4], [5, 6]])
    out1, out2 = feature_scaling(data)
    print(out1, out2) #([[-1.2247, -1.2247], [0.0, 0.0], [1.2247, 1.2247]], [[0.0, 0.0], [0.5, 0.5], [1.0, 1.0]])