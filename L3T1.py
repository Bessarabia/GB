#1. Реализовать функцию, принимающую два числа (позиционные аргументы)
# и выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def my_func(arg1, arg2):
    try:
        ar1 = int(arg1)
        ar2 = int(arg2)
        return ar1 / ar2
    except ZeroDivisionError:
        print("Division by 0")
        return
    except ValueError:
        print("Some fuzzy input")

arg1 = input("ar1: ")
arg2 = input("ar2: ")

print(my_func(arg1, arg2))
