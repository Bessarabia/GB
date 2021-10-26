# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

test_list = ['pdf', 'json', bin, 8, 3.14, True, False, None]
listLength = len(test_list)
counter = 0

while counter < listLength:
    print(type(test_list[counter]))
    counter += 1
    
