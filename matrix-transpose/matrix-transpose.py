import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)   # ensure it's a NumPy array
    return A.T


# this is normal we to transpose a matrix

# row=len(A)
# col=len(A[0])
# result=[[0]*row for _ in range(col)]
# for i in range(row):
#     for j in range(col):
#         result[j][i]=A[i][j]
# return result