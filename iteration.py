import numpy as np

def power(A, x):
    for i in range(50):
        x1 = A*x
        eigen = np.linalg.norm(x1)
        x1 = x1 / eigen
        x = x1
    return eigen, x

    

A = np.matrix('1, 3, 5; 5, 2, 0; 2, 1, 1')
x = np.matrix('1; 1; 1')

eigen, eigen_vector = power(A, x)
print(eigen)
print(eigen_vector)

eigen, eigen_vector = power(np.linalg.inv(A), x)
print(eigen)
print(eigen_vector)
