import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    P = np.mat(C).I @ np.mat(B) # P = C^-1 * B
    return P

if __name__=="__main__":
    B = [[1, 0, 0], 
            [0, 1, 0], 
            [0, 0, 1]]
    C = [[1, 2.3, 3], 
            [4.4, 25, 6], 
            [7.4, 8, 9]]
    P = transform_basis(B, C)
    print(P)
    '''
    expected
    output: [[-0.6772, -0.0126, 0.2342],
            [-0.0184, 0.0505, -0.0275],
            [0.5732, -0.0345, -0.0569]]
    '''