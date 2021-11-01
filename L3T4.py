#4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def vstepen(x, y):
    try:
        powered = x ** y
    except TypeError:
        return "Please revise your input. Mind the sign and type!"
    return powered

print(vstepen(None, -5))
