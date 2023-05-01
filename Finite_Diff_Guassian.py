import numpy as np

def gauss_elimination(matrix_A, matrix_B):
    n = len(matrix_A)
    
    for i in range(n):
        max_element_index = abs(matrix_A[i:, i]).argmax() + i
        if matrix_A[max_element_index, i] == 0:
            raise ValueError("Matrix is singular")
        
        if max_element_index != i:
            matrix_A[[i, max_element_index]] = matrix_A[[max_element_index, i]]
            matrix_B[[i, max_element_index]] = matrix_B[[max_element_index, i]]
        
        for j in range(i + 1, n):
            factor = matrix_A[j, i] / matrix_A[i, i]
            matrix_A[j, i:] -= factor * matrix_A[i, i:]
            matrix_B[j, 0] -= factor * matrix_B[i, 0]
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix_B[i, 0] / matrix_A[i, i]
        matrix_B[:i, 0] -= x[i] * matrix_A[:i, i]
    
    return x

if __name__ == "__main__":
    D1 = 98.98
    D2 = 78.67
    D3 = 13.86
    Ds = 12.87

    matrix_A = np.array([[D1, -1, 0, 0], [-1, D2, -1, 0], [0, -1, D3, -1], [0, 0, -1, Ds]], dtype=float)
    matrix_B = np.array([[120], [0], [0], [25]], dtype=float)
    
    thetas = gauss_elimination(matrix_A, matrix_B)
    
    print("Thetas:", thetas)
