import numpy as np
from scipy import sparse

# create a matrix
matrix = np.array([[0,0],[1,0],[0,3]])
print(matrix)

# create compressed sparce row (CSR) matrix
matrix_sparse = sparse.csr_matrix(matrix)
print(matrix_sparse)