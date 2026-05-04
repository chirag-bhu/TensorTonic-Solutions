import numpy as np

def one_hot(y, num_classes=None):
    """
    Convert integer labels y ∈ {0,...,K-1} into one-hot matrix of shape (N, K).
    """
    # Write code here
    row=len(y)
    if num_classes != None:
        col=num_classes
    else:
        col=max(y)+1
    

    matrix = np.zeros((row,col))
    for i in range(len(y)):
        r=i
        c=y[i]
        matrix[r][c]=1
    return matrix
        
        

        