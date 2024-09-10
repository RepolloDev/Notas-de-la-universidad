import numpy as np

A = [[52, 20, 25], [30, 50, 20], [18, 30, 55]]
B = [[4800], [5810], [5690]]

# invierte la matriz A
A_inv = np.linalg.inv(A)
# multiplica la matriz inversa por la matriz B
X = np.dot(A_inv, B)
# muestra el resultado
print(X)
