import numpy as np


def gauss_seidel(A, b, x_init, epsilon1=1e-2, epsilon2=1e-1, max_iterations=500):
    D = np.diag(np.diag(A))
    LU = A - D
    x = x_init
    D_inv = np.diag(1 / np.diag(D))

    for i in range(max_iterations):
        x_old = np.copy(x)

        for j in range(A.shape[0]):
            current_x = D_inv[j][j] * (b[j] - np.dot(LU[j,:], x))
            x[j] = current_x

        residue =  np.linalg.norm(b - np.dot(A, x))
        relative_distances = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x_old, ord=np.inf)

        print("It: " + str(i) +". Resíduo:  " + str(residue)+". Distâncias relativas: " + str(relative_distances))
        print("x = " + str(x))

        if residue < epsilon1 and relative_distances < epsilon2:
            print("Número de iterações total: " + str(i+1))
            return x

    return None


matrix_2 = []
for i in range(6):
    row = []
    for j in range(6):
        if i == j:
            row.append(-2)
        elif abs(i-j) == 1:
            row.append(0.5)
        else:
            row.append(0)

    matrix_2.append(row)

A2 = np.array(matrix_2)

matrix_3 = []
for i in range(6):
    row = []
    for j in range(6):
        if i == j:
            row.append(2)
        elif abs(i-j) == 1:
            row.append(2)
        else:
            row.append(0)

    matrix_3.append(row)

A3 = np.array(matrix_3)

# problem data
A1 = np.array([
    [2, -1, 0, 0, 0, 0],
    [-1, 2, -1, 0, 0, 0],
    [0, -1, 2, -1, 0, 0],
    [0, 0, -1, 2, -1, 0],
    [0, 0, 0, -1, 2, -1],
    [0, 0, 0, 0, -1, 2],
])
b = np.array([1, 1, 1, 1, 1, 1])

# you can choose any starting vector
x_init = np.zeros(len(b))
print(A3)
x = gauss_seidel(A1, b, x_init)

print("x:", x)