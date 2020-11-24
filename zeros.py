# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
from timebudget import timebudget


def bisseccao(function, a, b, stop_condition):
    return aux_bisseccao(function, a, b, stop_condition, 100, 0)


def aux_bisseccao(function, a, b, stop_condition, max_it, current_it):

    current_it = current_it + 1
    print(current_it)
    if function(a)*function(b) > 0:
        return False

    aux = (a+b)/2

    # Fizemos isso para poder comparar o sinal com um valor auxiliar de zero
    if aux == 0:
        aux = -0.000000000001

    r_aux = function(aux)

    if abs(a-b) < stop_condition or current_it >= max_it:
        return aux

    #se for exatamente 0, retornamos
    if function(aux) == 0.0:
        return aux

    if function(a) * function(aux) < 0:
        return aux_bisseccao(function, a, aux, stop_condition, max_it, current_it)
    elif function(b) * function(aux) < 0:

        return aux_bisseccao(function, aux, b, stop_condition, max_it, current_it)

    return False


def falsa_posicao(function, a, b, stop_condition):
    return aux_falsa_posicao(function, a, b, stop_condition, 100, 0)


def aux_falsa_posicao(function, a, b, stop_condition, max_it, current_it):

    current_it = current_it + 1
    print(current_it)
    if function(a)*function(b) > 0:
        return False

    aux = (a*function(b) - b*function(a))/(function(b) - function(a))

    r_aux = function(aux)

    # Fizemos isso para poder comparar o sinal com um valor auxiliar de zero
    if aux == 0:
        aux = 0.000000000001

    if abs(a-b) < stop_condition or current_it >= max_it:
        return aux

    # se for exatamente 0, retornamos
    if function(aux) == 0.0:
        return aux


    if function(a) * function(aux) < 0:
        return aux_falsa_posicao(function, a, aux, stop_condition, max_it, current_it)
    elif function(b) * function(aux) < 0:
        return aux_falsa_posicao(function, aux, b, stop_condition, max_it, current_it)

    return False

def f1(x):
    return -0.5*(x-2) + 1

def f2(x):
    return x ** 3 - 4*x + 2

def f3(x):
    return (x ** 3 - 4*x + 2) - (-0.5 * (x-2) + 1)

@timebudget
def run():
    return bisseccao(f3, 1, 3, 0.001)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(run())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
