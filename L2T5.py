 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
#!я так понял, что не возрастающий, это, как в примере, всё-таки убывающий, но не произвольный!
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.

# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
userInt = int(input("Please enter your rating here: "))

listLen = len(my_list)
iterator: int = 0

while iterator < listLen:
    if userInt > int(my_list[iterator]):
        print(f'{userInt}{" was added before "}{my_list[iterator]}')
        my_list.insert(iterator, userInt)
        break
    if userInt == int(my_list[iterator]):
       if iterator == listLen - 1:
        print(f'{userInt}{" was added after "}{my_list[iterator]}')
        my_list.append(userInt)
        break
       if userInt < my_list[iterator + 1]:
        print(f'{userInt}{" was added after "}{my_list[iterator]}')
        my_list.insert(iterator + 1, userInt)
        break
    iterator += 1
if userInt < int(my_list[listLen-1]):
    my_list.append(userInt)
    print(f'{userInt}{" was added after "}{my_list[listLen-1]}')
print(my_list)
