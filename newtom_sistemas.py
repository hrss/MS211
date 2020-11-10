import numpy as np
from sympy import symbols, diff, N


def get_F(n_x, n_y):
    x, y = symbols('x y', real=True)
    f1 = (x - 3) ** 2 + (y + 1) ** 2 - 16
    f2 = y ** 2 - x + 1
    return np.array([f1.evalf(subs={x: n_x, y: n_y}), f2.evalf(subs={x: n_x, y: n_y})]).transpose()


def get_jacobian(n_x, n_y):
    x, y = symbols('x y', real=True)
    f1 = (x - 3) ** 2 + (y + 1) ** 2 - 16
    f2 = y ** 2 - x + 1

    d11 = diff(f1, x)
    d12 = diff(f1, y)
    d21 = diff(f2, x)
    d22 = diff(f2, y)

    return np.array([[d11.evalf(subs={x: n_x, y: n_y}), d12.evalf(subs={x: n_x, y: n_y})],
                     [d21.evalf(subs={x: n_x, y: n_y}), d22.evalf(subs={x: n_x, y: n_y})]], dtype='float')


def newton_sistemas(x_init, epsilon=1e-2, max_iterations=500):
    x = x_init

    for i in range(max_iterations):
        x_new = x - np.linalg.inv(get_jacobian(x[0], x[1])).dot(get_F(x[0], x[1]))
        residue = np.linalg.norm(get_F(x_new[0], x_new[1]), ord=np.inf)
        print("It: " + str(i) + ". Resíduo:  " + str(residue) + ".")
        print("x = " + str(x_new))
        if residue < epsilon:
            print("Número de iterações total: " + str(i + 1))
            return x_new
        x = x_new

newton_sistemas(np.array([2, 0.5]))
newton_sistemas(np.array([4, -2]))