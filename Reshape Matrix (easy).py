import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    reshaped_matrix = np.reshape(a, new_shape)
    return reshaped_matrix

if __name__=="__main__":
    a = [[1,2,3,4],[5,6,7,8]]
    new_shape = (4, 2)
    print(reshape_matrix(a,new_shape))
