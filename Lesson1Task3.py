#Узнайте у пользователя число n. Найдите сумму чисел n +
#nn + n Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369
baseNumber=input("Input base number ")
n = int(baseNumber)
nn = int(baseNumber+baseNumber)
nnn = int(baseNumber+baseNumber+baseNumber)
execSum = n + nn + nnn
print(f"{n} + {nn}+{nnn} = {execSum}")
