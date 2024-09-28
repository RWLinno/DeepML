import numpy as np

def svd_2x2_singular_values(A):
    A = np.mat(A)
    A_T_A = A.T @ A
    theta = 0.5 * np.arctan2(2 * A_T_A[0, 1], A_T_A[0, 0] - A_T_A[1, 1])
    j = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    A_prime = j.T @ A_T_A @ j 
    
    # Calculate singular values from the diagonalized A^TA (approximation for 2x2 case)
    singular_values = np.sqrt(np.diag(A_prime))

    # Process for AA^T, if needed, similar to A^TA can be added here for completeness
    
    return j, singular_values, j.T

if __name__=="__main__":
    a = [[2, 1], [1, 2]]
    print(svd_2x2_singular_values(a))
  
'''
Example:
        input: a = [[2, 1], [1, 2]]
        output: (array([[-0.70710678, -0.70710678],
                        [-0.70710678,  0.70710678]]),
        array([3., 1.]),
        array([[-0.70710678, -0.70710678],
               [-0.70710678,  0.70710678]]))
        reasoning: U is the first matrix sigma is the second vector and V is the third matrix
'''