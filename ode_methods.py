import matplotlib.pyplot as plt
import math
import sys
sys.setrecursionlimit(3000)

##Explicit
def euler_explicit(y0, x0, x_final, h, derivative_function,xs,ys, max_it, range_low, range_high):
    it = 0
    while x0 <= x_final and it < max_it:
        y_d0 = derivative_function(x0, y0)
        y0 = y0 + y_d0 * h
        x0 = h + x0
        ys.append(y0)
        xs.append(x0)
        it += 1

        if range_low is not None and range_high is not None:
            if range_low < abs(y0) < range_high:
                print(it)
                return y0

    print(it)
    return y0


def derivative_function(x, y):
    #print(y ** 2)
    return y + math.cos(y) - x
    #return y


##### Implicit
def euler_implicit(y0, x0, x_final, h ,xs,ys, max_it, range_low, range_high):
    it = 0
    total_it = 0
    while x0 <= x_final and it < max_it:
        y0, total_it = newton(y0, newton_function, h, x0, y0, newton_derivative, 1000, 0, 1e-5, 1e-3, total_it)
        x0 = x0 + h
        it += 1
        xs.append(x0)
        ys.append(y0)

        if range_low is not None and range_high is not None:
            if range_low < abs(y0) < range_high:
                print(it)
                return y0
    print(it)
    print(total_it)
    return y0

def newton(y, function, h, x, y0 , d_func, max_iterations, current_it, tol1, tol2, total_it):
    current_it = current_it + 1
    total_it = total_it + 1
    new_y = y - (function(y, h, x, y0)/d_func(y, h))

    if abs(function(new_y, h, x, y0)) < tol2 and abs(new_y - y) < tol1 or current_it > max_iterations:
        return new_y, total_it

    return newton(new_y, function, h, x, y0, d_func, max_iterations, current_it, tol1, tol2, total_it)


def newton_function(y, h, x, y0):
    return y - h*(y + math.cos(y) - x) - y0#y - h * y ** 2 - y0#


def newton_derivative(y, h):
    return 1 - h * (1 - math.sin(y))#1 - h * y ** 2#


### Runge Kutta
def euler_runge_kutta(y0, x0, x_final, h, derivative_function, xs,ys, max_it, range_low, range_high):
    it = 0
    while x0 <= x_final and it < max_it:

        k1 = derivative_function(x0, y0)
        k2 =derivative_function(x0 + h, y0 + h*k1)
        y0 = y0 + h*k2
        x0 = h + x0
        ys.append(y0)
        xs.append(x0)
        it += 1
        if range_low is not None and range_high is not None:
            if range_low < abs(y0) < range_high:
                print(it)
                return y0
    print(it)
    return y0

xs = [1]
ys = [2]


### Para rodar sem verificar o range de erro ###

#print(euler_runge_kutta(2, 1, 5, 1e-4, derivative_function, xs, ys, 50000000, None, None))
#print(euler_explicit(2, 1, 5, 1e-4, derivative_function, xs, ys, 500000000000, None, None))
#print(euler_implicit(2, 1, 5, 1e-4, xs, ys, 5000090, None, None))



### Para rodar verificar o range de erro ###

#print(euler_runge_kutta(2, 1, 5, 1e-5, derivative_function, xs, ys, 50000000, 11.695, 11.895))
#print(euler_explicit(2, 1, 5, 1e-4, derivative_function, xs, ys, 500000000000, 11.695, 11.895))
print(euler_implicit(2, 1, 5, 1e-4, xs, ys, 5000090, 11.695, 11.895))

plt.plot(xs, ys)
plt.legend(['Euler implicito'])
plt.grid(True)
plt.show()

# y' =  y + cos(y) - x
# y'= y = eˆx