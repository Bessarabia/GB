#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. (result_list.insert(pos, el) Разместить на позиции pos (индекс элемента списка) элемент el
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

userList = []
while True:
    userString = input("Введите значение элемента списка, или завершите его создание просто нажав Enter ")
    if not bool(userString):
        break
    else:
        userList.append(userString)
    continue

print(userList)
listLength = (len(userList))
resultList = []
iterator = 1
while iterator < listLength:
    swap1 = userList[iterator - 1]
    swap2 = userList[iterator]
    resultList.append(swap2)
    resultList.append(swap1)
    print(swap1, swap2, "swap ok")
    iterator += 2

if not (listLength % 2 == 0):
    resultList.append(userList[listLength-1])
print(resultList)
