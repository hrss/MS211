import math


def newton(x, function, d_func, max_iterations, current_it, tol1, tol2):
    current_it = current_it + 1
    print(current_it)
    new_x = x - (function(x)/d_func(x))

    if abs(function(new_x)) < tol2 and abs(new_x - x) < tol1 or current_it > max_iterations:
        return new_x

    return newton(new_x, function, d_func, max_iterations, current_it, tol1, tol2)


def function(x):
    return math.sin(x) - x + 1


def derivative(x):
    return math.cos(x) - 1


print(newton(math.pi/4, function, derivative, 1000, 0, 1e-5, 1e-3))
